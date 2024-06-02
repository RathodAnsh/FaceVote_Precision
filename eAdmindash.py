from tkinter import *
from tkinter import Tk
from subprocess import call
import tkinter.messagebox as messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

root=Tk()
root.geometry("800x730")



def move_to_verify_cand():
      root.destroy()
      call(["python","everifycand.py"])

def move_to_add_voter():
      root.destroy()
      call(["python","eaddvoter.py"])

def move_to_deresult():
      root.destroy()
      call(["python","eadmindeclareresult.py"])

def move_to_admin_log():
    confirm=messagebox.askyesno("Logout","Are you sure you want to logout")
    if confirm:
       root.destroy()
       call(["python","eadminlog.py"])       


def toggel_menu():

    def destroy_menu():
        menu_frame.destroy()
        toggle_btn.config(text="≡",font="Arial 22")
        toggle_btn.config(command=toggel_menu)

    menu_frame=Frame(last_frame,bg="Blue",height=350,width=200,bd=5,relief=GROOVE)
    menu_frame.place(y=0)

    toggle_btn.config(text="x",font="Candara 20")
    toggle_btn.config(command=destroy_menu)

    Cand_verify=Button(menu_frame,text="Verify Candidate",bd=2,bg="Light Gray",fg="Black",font="cooper 14 bold",command=move_to_verify_cand)
    Cand_verify.place(x=9,y=50)

    #add_voter=Button(menu_frame,text="Add Voter",bd=2,bg="Light Gray",fg="Black",font="cooper 14 bold",width=13,command=move_to_add_voter)
    #add_voter.place(x=10,y=145)

    result_btn=Button(menu_frame,text="Result",bd=2,bg="Light Gray",fg="Black",font="cooper 14 bold",width=13,command=move_to_deresult)
    result_btn.place(x=9,y=145)


    
frame=Frame(root,width=780,height=105,bg="Light Blue")
frame.place(x=40,y=0)
label=Label(frame, text="Face Vote Precision", font="Arial 32 ", background="Light Blue")
label.place(x=60,y=26)

#backbtn=Button(frame,text="Back",bg="blue",fg="white",font="BerlinSans 15 bold")
#backbtn.place(x=680,y=30)

image=Image.open("lg.png_-removebg-preview.png")
image = image.resize((100,102))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo,background="Light blue")
logo_label.place(x=0,y=0)

margin_frame = Frame(root,width=800,height=4,background="Black")  # Adjust the height 
margin_frame.place(y=105)

frame2=Frame(root,width=800,height=55,bg="Light Gray")
frame2.place(y=107)

margin_frame = Frame(frame2,width=1700,height=1,background="Black")  # Adjust the height 
margin_frame.place(y=54)

toggle_btn=Button(frame2,text="≡",font="Arial 22 ",bg="Light Gray",bd=0,command=toggel_menu)
toggle_btn.place(x=5)

admin_label=Label(frame2,text="Admin Portal",font="Rockwell 24  ",bg="Light Gray",bd=0)
admin_label.place(x=60,y=7)

image=Image.open("logout-removebg-preview.png")
image = image.resize((40,40))
photo2=ImageTk.PhotoImage(image)
logo_label=Label(frame2,image=photo2,background="Light gray")
logo_label.place(x=675,y=4)

Cand_logout=Button(frame2,text="Logout",background="Light Gray",fg="Black",font="calibri 15 bold",border=0,bd=0,height=1,width=6,command=move_to_admin_log)
Cand_logout.place(x=720,y=6)

last_frame=Frame(root,bg="Gray")
last_frame.place(y=162,height=520,width=800)

search_frame=Frame(last_frame,highlightbackground="Black",highlightthickness=1)
search_frame.pack(side=TOP,fill=X)
search_frame.configure(width=800,height=45)

search_lable=Label(search_frame,text="Search:-",fg="Black",bd=0,font="Arial 15 bold")
search_lable.place(x=160,y=8)

search_txt=Entry(search_frame,bg="white",width=25,font=('Arial',14),bd=2)
search_txt.place(x=260,y=8)

#===================================================searching candidate=================================================

def search_candidate():
    search_term = search_txt.get()
    if search_term:
        for row in cand_table.get_children():
            if cand_table.item(row)['values'][0] == search_term:  # Assuming voter ID is in the first column
                cand_table.selection_set(row)
                cand_table.focus(row)
                break
    else:
        messagebox.showwarning("Empty Search", "Please enter a voter ID to search.")

search_btn=Button(search_frame,text="Search",bg="Light Gray",fg="Black",font=('Arial',12,'bold'),command=search_candidate)
search_btn.place(x=550,y=4)

#show_btn=Button(search_frame,text="Show all",bg="Light Gray",fg="Black",font=('Arial',12,'bold'))
#show_btn.place(x=600,y=4)

table_frame=Frame(last_frame,highlightbackground="Black",highlightthickness=2,bg="white",bd=7,relief=GROOVE)
table_frame.pack(fill=BOTH,expand=True)

style = ttk.Style()
style.configure("Treeview", font=("Arial", 11)) 
style.configure("Treeview.Heading", font=("Arial 13 bold"))


y_scroll=Scrollbar(table_frame,orient=VERTICAL)
x_scroll=Scrollbar(table_frame,orient=HORIZONTAL)

cand_table=ttk.Treeview(table_frame,columns=("voter_id","name","gender","age","dob","p_name"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set,height=50)

y_scroll.config(command=cand_table.yview)
x_scroll.config(command=cand_table.xview)
y_scroll.pack(side=RIGHT,fill=Y)
x_scroll.pack(side=BOTTOM,fill=X)

cand_table.heading("voter_id",text="Voter Id")
cand_table.heading("name",text="Name")
cand_table.heading("gender",text="Gender")
cand_table.heading("age",text="Age")
cand_table.heading("dob",text="Date of Birth")
cand_table.heading("p_name",text="Party name")

cand_table['show']='headings'

cand_table.column("voter_id",width=120)
cand_table.column("name",width=250)
cand_table.column("gender",width=100)
cand_table.column("age",width=50)
cand_table.column("dob",width=150)
cand_table.column("p_name",width=250)

cand_table.pack(fill=BOTH,expand=True)

#==============================================Fetching data into table============================================
def fetch_main_candidate_data():
      try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ansh@7514",
        database="admin1"
    )
        cursor = connection.cursor()
        cursor.execute("Select Voter_id,Name,Gender,Age,Dob,Address,P_name from Candidate_main")
        data=cursor.fetchall()

        if len(data)!=0:
             cand_table.delete(*cand_table.get_children())
             for row in data:

                  cand_table.insert("",END,values=(row[0], row[1], row[2], row[3], row[4], row[6]))
             connection.commit()
        connection.close()     

      except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")
            
      finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to delete a candidate from GUI and database
def delete_candidate():
    # Get the selected item from the treeview
    selected_item = cand_table.focus()
    if not selected_item:
        messagebox.showwarning("No Candidate Selected", "Please select a candidate to disqualify.")
        return

    # Get the candidate ID from the selected item
    candidate_id = cand_table.item(selected_item)['values'][0]

    # Confirm deletion with the user
    confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to disqualify this candidate?")
    if confirm:
        try:
            # Connect to the database
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ansh@7514",
                database="admin1"
            )
            cursor = connection.cursor()

            # Delete the candidate from the database
            cursor.execute("DELETE FROM Candidate_main WHERE Voter_id = %s", (candidate_id,))

            cursor.execute("DELETE FROM Candidatereg WHERE Voter_id = %s", (candidate_id,))

            cursor.execute("DELETE FROM enrolled_once WHERE Voter_id = %s", (candidate_id,))
            connection.commit()

            # Delete the candidate from the GUI
            cand_table.delete(selected_item)

            messagebox.showinfo("Deletion Successful", "Candidate has been disqualified successfully.")
        except mysql.connector.Error as error:
            messagebox.showerror("Database Error", f"Failed to delete candidate: {error}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

# Button to disqualify candidate

delete_cand=Button(root,text="Disqualify Candidate",bd=2,bg="Gray",fg="Black",font="cooper 12 bold",command=delete_candidate)
delete_cand.place(x=600,y=690)

fetch_main_candidate_data()
       
root.mainloop()