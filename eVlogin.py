from tkinter import *
from tkinter import Tk
from subprocess import call
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

def Voter_login():
    
    #Get user entry
    voterid=username1.get()
    password_entry=password1.get()

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
            messagebox.showinfo("Success", "Successfully Login!!")
            root.destroy()
            call(['python', "eVote.py",voterid])
        else:
            messagebox.showerror("Error", "Please Enter valid credential")   



    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")
            
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


root=Tk()
root.geometry("700x600")


    

def move_to_old_login():
    root.destroy()
    call(['python', "eoldlogin.py"]) 

def move_to_voter_portal():
    root.destroy()
    call(['python', "eVoterportal.py"])       

frame=Frame(root,width=700,height=95,bg="Light Blue")
frame.place(x=40,y=0)
label=Label(frame, text="Face Vote Precision", font="Arial 30 ", background="Light Blue")
label.place(x=50,y=20)

image=Image.open("lg.png_-removebg-preview.png")
image = image.resize((90,90))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo,background="Light blue")
logo_label.place(x=0,y=0)

cross_btn=Button(frame,text="x",bg="Light Blue",fg="Black",font="Candara 15 bold",border=0,command=move_to_voter_portal)
cross_btn.place(x=635,y=0)

margin_frame = Frame(root,width=1700,background="Black")  # Adjust the height 
margin_frame.place(y=95)

admin_lable=Label(root,text="Voter Login",bg="white",fg="Black",font="Rockwell 22 bold")
admin_lable.place(x=285,y=105)

frame1=Frame(root,background="Light Blue",height=390,width=540)
frame1.place(x=82,y=150)

image=Image.open("log-removebg-preview.png")
image = image.resize((140,105))
photo1=ImageTk.PhotoImage(image)
logo_label=Label(frame1,image=photo1,background="Light blue")
logo_label.place(x=221,y=0)


username1=Label(frame1,text="Username :- ",foreground="Black",background="Light Blue",fg="Black",font="Times 18 ",border=0)
username1.place(x=90,y=120)
username1=Entry(frame1,foreground="Black",background="White",font="Times 14 ",border=0,bd=2,width=25)
username1.place(x=220,y=120)

password1=Label(frame1,text="Password  :- ",foreground="Black",background="Light Blue",font="Times 18 ",border=0)
password1.place(x=90,y=185)
password1=Entry(frame1,foreground="Black",background="White",font="Times 14 ",border=0,bd=2,show="*",width=25)
password1.place(x=220,y=185)

log_btn=Button(frame1,text="Log In", foreground="White",background="Blue",font="Candara 16 bold",command=Voter_login)
log_btn.place(x=240,y=260)

lable=Label(frame1,text="Not Registered ?",fg="Black",bg="Light Blue",font="Calibri 15",border=NO)
lable.place(x=180,y=340)

reg_btn=Button(frame1,text="Register",fg="Blue",bg="Light Blue",font="calibri 15 bold underline",border=0,cursor="hand2",command=move_to_old_login)
reg_btn.place(x=320,y=332)


root.mainloop()