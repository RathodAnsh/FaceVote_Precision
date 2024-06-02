from tkinter import *
from tkinter import Tk, messagebox
from subprocess import call
from PIL import Image, ImageTk
from tkinter import ttk
import datetime

root = Tk()
root.geometry("800x780")

start_time = None
end_time = None
vote_btn = None
logged_in = False
election_started = False

# Function to read the election status from a file
def read_election_status():
    try:
        with open("election_status.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "not_started"

# Function to enable/disable the "Vote" button based on the election status
def update_vote_button_state():
    global vote_btn
    if vote_btn:
        election_status = read_election_status()
        if election_status == "started":
            vote_btn.config(state="normal")
        else:
            vote_btn.config(state="disabled")

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

# Save start and end times to a file
def save_times():
    try:
        with open("election_times.txt", "w") as file:
            file.write(start_time.strftime("%H:%M") + "\n")
            file.write(end_time.strftime("%H:%M") + "\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def move_to_cand_list():
    root.destroy()
    call(["python", "ecandlist.py"])

def move_to_voter_list():
    root.destroy()
    call(["python", "evoterlist.py"])

def move_to_declare():
    root.destroy()
    call(["python", "emanagedeclare.py"])

def move_to_manage_log():
    global logged_in
    confirm = messagebox.askyesno("Logout", "Are you sure you want to logout")
    if confirm:
        logged_in = False
        root.destroy()
        call(["python", "emanagementlog.py"])

def set_vote_button_status(enabled):
    if enabled:
        vote_btn.config(state="normal")
    else:
        vote_btn.config(state="disabled")

# Function to start the election
def start_election():
    global start_time, end_time, election_started
    current_time = datetime.datetime.now().time()

    if start_time is None or end_time is None:
        messagebox.showinfo("Error", "Please set start and end times first!")
        return

    if current_time < start_time:
        messagebox.showinfo("Election Not Started", "Election has not started yet.")
    elif current_time >= end_time:
        messagebox.showinfo("Election Ended", "Election has ended.")
    else:
        messagebox.showinfo("Election Started", "Election has started.")
        # Update the election status file to indicate that the election has started
        with open("election_status.txt", "w") as file:
            file.write("started")

        election_started = True
        update_vote_button_state()  # Call update_vote_button_state after the election starts

start_election_btn = Button(root, text="Start Election", bg="Green", fg="White", font="Candara 20 bold", command=start_election)
start_election_btn.place(x=320, y=410)

def set_start_time():
    try:
        global start_time
        start_time_str = start_entry.get().strip()  # Remove leading/trailing spaces
        start_time = datetime.datetime.strptime(start_time_str, "%H:%M").time()
    except ValueError:
        messagebox.showerror("Error", "Invalid start time format. Please enter time in HH:MM format.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def set_end_time():
    try:
        global end_time
        end_time_str = end_entry.get().strip()  # Remove leading/trailing spaces
        end_time = datetime.datetime.strptime(end_time_str, "%H:%M").time()
        save_times()  # Save the end time
    except ValueError:
        messagebox.showerror("Error", "Invalid end time format. Please enter time in HH:MM format.")

frame = Frame(root, width=780, height=105, bg="Light Blue")
frame.place(x=40, y=0)
label = Label(frame, text="Face Vote Precision", font="Arial 32 ", background="Light Blue")
label.place(x=60, y=26)

image = Image.open("lg.png_-removebg-preview.png")
image = image.resize((100,102))
photo = ImageTk.PhotoImage(image)
logo_label = Label(image=photo, background="Light blue")
logo_label.place(x=0, y=0)

margin_frame = Frame(root, width=800, height=4, background="Black")  # Adjust the height 
margin_frame.place(y=105)

frame2 = Frame(root, width=800, height=55, bg="Light Gray")
frame2.place(y=107)

margin_frame = Frame(frame2, width=1700, height=1, background="Black")  # Adjust the height 
margin_frame.place(y=54)

admin_label = Label(frame2, text="Election Management", font="Rockwell 24  ", bg="Light Gray", bd=0)
admin_label.place(x=250, y=7)

image = Image.open("logout-removebg-preview.png")
image = image.resize((40,40))
photo2 = ImageTk.PhotoImage(image)
logo_label = Label(frame2, image=photo2, background="Light gray")
logo_label.place(x=0, y=4)

management_logout = Button(frame2, text="Logout", background="Light Gray", fg="Black", font="calibri 15 bold", border=0, bd=0, height=1, width=6, command=move_to_manage_log)
management_logout.place(x=45, y=6)

button_frame = Frame(root, highlightbackground="Black", highlightthickness=2, bg="light green")
button_frame.place(y=160, width=800, height=100)

view_voter = Button(button_frame, text="Voters list", bd=2, font="Candara 14 bold", command=move_to_voter_list)
view_cand = Button(button_frame, text="Candidate list", bd=2, font="Candara 14 bold", command=move_to_cand_list)
result_declare = Button(button_frame, text="Declare result", bd=2, font="Candara 14 bold", command=move_to_declare)
view_voter.place(x=90, y=30, width=160)
view_cand.place(x=320, y=30, width=160)
result_declare.place(x=550, y=30, width=160)

start_label = Label(root, text="Set Start Time (HH:MM):")
start_label.place(x=200, y=520)
start_entry = Entry(root)
start_entry.place(x=400, y=520)
start_button = Button(root, text="Set", command=set_start_time)
start_button.place(x=600, y=515)

end_label = Label(root, text="Set End Time (HH:MM):")
end_label.place(x=200, y=560)
end_entry = Entry(root)
end_entry.place(x=400, y=560)
end_button = Button(root, text="Set", command=set_end_time)
end_button.place(x=600, y=555)

# Load times and check if the election has started
load_times()
current_time = datetime.datetime.now().time()
if start_time and end_time and start_time <= current_time <= end_time:
    election_started = True
    update_vote_button_state()  # Call update_vote_button_state after checking election status

root.mainloop()
