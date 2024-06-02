from tkinter import *
from tkinter import Tk
from subprocess import call
import mysql.connector
from tkinter import messagebox

def candidate_entry():
    #Get user entry
    voterid=username.get()
    password_entry=password.get()

    if not voterid and not password_entry:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ansh@7514",
        database="voter"
    )
        cursor = connection.cursor()
        select_query="SELECT * FROM register_detail WHERE Voterid=%s and Password=%s "
        enter_data=(voterid,password_entry)
        cursor.execute(select_query,enter_data)
        row=cursor.fetchone()

        if row:
            messagebox.showinfo("Success", "Successfully verified for registration")
            root.destroy()
            call(["python","ecandreg.py",voterid])
        else:
            messagebox.showerror("Error", "Please Enter valid credential")   



    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")
            
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

root=Tk()
root.geometry("700x400")

def move_to_cand_portal():
    root.destroy()
    call(["python","eCandidateportal.py"])    

lable=Label(root,text="Register here",foreground="Black",font="Rockwell 24 bold underline")
lable.pack(pady=(15,0))

frame=Frame(root,width=550,height=270,bg="Light Blue")
frame.place(x=74,y=80)

lable=Label(frame,text="Register Using VoterID and Password",foreground="Black",background="Light Blue",font="Rockwell 19 bold",border=0)
lable.place(x=60,y=10)

username=Label(frame,text="Voter ID :- ",foreground="Black",background="Light Blue",fg="Black",font="Times 18 ",border=0)
username.place(x=110,y=90)
username=Entry(frame,foreground="Black",background="White",font="Times 14 ",border=0,bd=2,width=25)
username.place(x=240,y=90)

password=Label(frame,text="Password  :- ",foreground="Black",background="Light Blue",font="Times 18 ",border=0)
password.place(x=110,y=150)
password=Entry(frame,foreground="Black",background="White",font="Times 14 ",border=0,bd=2,show="*",width=25)
password.place(x=240,y=150)

confirm_btn= Button(frame,text="Confirm", foreground="White",background="Blue",font="Candara 16 bold",border=0,bd=1,command=candidate_entry)
confirm_btn.place(x=190,y=200)

back_btn= Button(frame,text="Back", foreground="White",background="Blue",font="Candara 16 bold",border=0,bd=1,command=move_to_cand_portal)
back_btn.place(x=335,y=200)






root.mainloop()