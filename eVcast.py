from tkinter import *
from tkinter import Tk, ttk, messagebox
from subprocess import call
from PIL import Image, ImageTk
import mysql.connector
import sys
import cv2
import datetime

# Global variables
vote_btn = None
start_time = None
end_time = None
voted = False
model_loaded = False

if len(sys.argv) > 1:
    Voter_id = sys.argv[1]
else:
    print("Error: Voter ID not provided.")
    sys.exit(1)  

# Function to read the election status from a file
def read_election_status():
    try:
        with open("election_status.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "not_started"

# Function to enable/disable the "Vote" button based on the election status
def update_vote_button_state():
    global vote_btn, start_time, end_time
    election_status = read_election_status()
    current_time = datetime.datetime.now().time()  # Get the current time
    if election_status == "started" and start_time <= current_time < end_time:
        vote_btn.config(state="normal")  # Enable the vote button if election is ongoing
    else:
        vote_btn.config(state="disabled")  # Disable the vote button otherwise

def move_to_main_vote():
    root.destroy()
    call(['python', "eVote.py", Voter_id])

def vote_scan():
    root.destroy()
    call(['python', "evotescan.py"])  

def vote_selected_row():
    global voted, model_loaded

    # Check if the face recognition model is loaded
    if not model_loaded:
        messagebox.showinfo("Error", "First generate your dataset then vote.")
        return

    # Check if the voter has already voted
    if voted:
        messagebox.showinfo("Error", "You have previously voted.")
        return

    selected_items = cand_table.selection()
    if not selected_items:
        # No candidate selected, display message
        messagebox.showinfo("Error", "Please select a candidate to vote for.")
        return

    voter_ids = [cand_table.item(item, 'values')[0] for item in selected_items]

    # Start face detection process
    for voter_id in voter_ids:
        selected_row = next((item for item in selected_items if cand_table.item(item, 'values')[0] == voter_id), None)
        if selected_row:
            candidate_name = cand_table.item(selected_row, 'values')[1]
            party_name = cand_table.item(selected_row, 'values')[2]

            # Proceed with face detection
            vote_result = detect_face_and_vote(voter_id, candidate_name, party_name)
            if vote_result:
                # If voting is successful, show success message and mark as voted
                messagebox.showinfo("Success", "Voted Successfully")
                voted = True
            else:
                # If face detection fails, show error message
                messagebox.showinfo("Error", "Face not detected. Please try again.")

def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf, voter_id, candidate_name, party_name):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        id, pred = clf.predict(gray_image[y:y + h, x:x + w])
        confidence = int(100 * (1 - pred / 300))

        if confidence > 80:
            # Insert the vote into the database
            insert_vote(voter_id, candidate_name, party_name)
            return True
        else:
            return False

def detect_face_and_vote(voter_id, candidate_name, party_name):
    global model_loaded
    if not model_loaded:
        messagebox.showinfo("Error", "First Generate Your Dataset")
        return False
    
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, img = video_capture.read()
        cv2.imshow("Face Detection", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if ret:
            if draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf, voter_id, candidate_name, party_name):
                video_capture.release()
                cv2.destroyAllWindows()
                return True
            else:
                video_capture.release()
                cv2.destroyAllWindows()
                return False

def insert_vote(voter_id, candidate_name, party_name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ansh@7514",
            database="admin1"
        )
        cursor = connection.cursor()

        # Insert the vote into the database
        insert_query = "INSERT INTO casted_vote (V_id, C_name, P_name) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (voter_id, candidate_name, party_name))

        connection.commit()
    except mysql.connector.Error as error:
        print("Error inserting record into MySQL table:", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def fetch_party_data():
    global model_loaded  # Add this line to access the global variable

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ansh@7514",
            database="admin1"
        )
        cursor = connection.cursor()
        cursor.execute("Select Voter_id,Name,P_name from Candidate_main")
        data = cursor.fetchall()

        if len(data) != 0:
            cand_table.delete(*cand_table.get_children())
            for row in data:
                cand_table.insert("", END, values=(row[0], row[1], row[2]))
            connection.commit()

            # Update model_loaded flag since dataset is generated
            model_loaded = True  # Set model_loaded to True

        connection.close()

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")


def view_selected_row():
    selected_item = cand_table.focus()
    if selected_item:
        selected_row = cand_table.item(selected_item, 'values')
        voter_id = selected_row[0]  # Get the voter ID from the selected row
      
        call(['python', 'eviewparty.py', voter_id])
    else:
        messagebox.showinfo("Error","To view detail select one row")

def load_times():
    global start_time, end_time
    try:
        with open("election_times.txt", "r") as file:
            times = file.readlines()
            if len(times) >= 2:
                start_time = datetime.datetime.strptime(times[0].strip(), "%H:%M").time()
                end_time = datetime.datetime.strptime(times[1].strip(), "%H:%M").time()
            else:
                messagebox.showerror("Error", "Please set start and end times first!")
    except FileNotFoundError:
        messagebox.showerror("Error", "Start and end times file not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root=Tk()
root.geometry("800x780")

# Background frame
background_frame = Frame(root, bg="Light Blue")
background_frame.pack(fill=X)
label = Label(background_frame, text="Face Vote Precision", foreground="black", font="Arial 33 ", background="Light Blue")
label.pack(padx=(0, 150), pady=(28,25))

# Logo
image=Image.open("lg.png_-removebg-preview.png")
image = image.resize((110,100))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo,background="Light blue")
logo_label.place(x=0,y=5)

# Back button
backbtn=Button(text="Back",bg="blue",fg="white",font="BerlinSans 15 bold",command=move_to_main_vote)
backbtn.place(x=720,y=33)

# Margin frame
margin_frame = Frame(root,width=1700,background="Black")
margin_frame.place(y=110)

# Head label
head_label=Label(root,text="Vote for Better future",font="Rockwell 24  ",bg="White",bd=0)
head_label.place(x=260,y=115)

# Fetched ID label
fetched_id=Label(root,text=Voter_id,font="Rockwell 15  ",bg="White",bd=0)
fetched_id.place(x=40,y=160)

# Main frame
main_frame=Frame(root,bg="Gray")
main_frame.place(y=160,height=530,width=800)

# Style for Treeview
style = ttk.Style()
style.configure("Treeview", font=("Arial", 11)) 
style.configure("Treeview.Heading", font=("Arial 13 bold"))

# Table frame
table_frame=Frame(main_frame,highlightbackground="Black",highlightthickness=2,bg="white",bd=7,relief=GROOVE)
table_frame.pack(fill=BOTH,expand=True)

# Scrollbars
y_scroll=Scrollbar(table_frame,orient=VERTICAL)
x_scroll=Scrollbar(table_frame,orient=HORIZONTAL)

cand_table=ttk.Treeview(table_frame,columns=("voter_id","name","p_name"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set,height=50)

y_scroll.config(command=cand_table.yview)
x_scroll.config(command=cand_table.xview)
y_scroll.pack(side=RIGHT,fill=Y)
x_scroll.pack(side=BOTTOM,fill=X)

cand_table.heading("voter_id",text="Voter Id")
cand_table.heading("name",text="Name")
cand_table.heading("p_name",text="Party Name")

cand_table['show']='headings'

cand_table.column("voter_id",width=120)
cand_table.column("name",width=270)
cand_table.column("p_name",width=280)

cand_table.pack(fill=BOTH,expand=True)

# Fetching data into table
fetch_party_data()

# Button to view selected candidate
view_button = Button(root, text="View selected candidate", bg="Light Green", font="cooper 15 bold", command=view_selected_row)
view_button.place(x=100, y=710, height=30, width=240)

# Load election times
load_times()

# Function to handle voting
def handle_voting():
    global voted
    if voted:
        messagebox.showinfo("Error", "You have previously voted.")
    else:
        vote_selected_row()

# Button to vote
vote_btn = Button(root, text="Vote", bg="Light Green", font="Candara 15 bold", command=handle_voting, state="disabled")
vote_btn.place(x=355, y=705, width=120)

# Update the state of the "Vote" button
update_vote_button_state()

root.mainloop()
