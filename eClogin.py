from tkinter import *
from tkinter import Tk
from subprocess import call
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

def Candidate_login():
    
    #Get user entry
    voterid=cand_username.get()
    password_entry=cand_password.get()

    if not voterid and not password_entry:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    
    
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ansh@7514",
        database="admin1"
    )
        cursor = connection.cursor()
        select_query="SELECT * FROM candidatereg WHERE Voter_id=%s and password=%s "
        enter_data=(voterid,password_entry)
        cursor.execute(select_query,enter_data)
        row=cursor.fetchone()

        if row:
            messagebox.showinfo("Success", "Successfully Login!!")
            root.destroy()
            call(["python","eCandenroll.py",voterid]) 
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

    

def move_to_cand_regentry():
    root.destroy()
    call(["python","eCregentry.py"])

def move_to_cand_portal():
    root.destroy()
    call(["python","eCandidateportal.py"])        


        


frame=Frame(root,width=700,height=95,bg="Light Blue")
frame.place(x=40,y=0)
label=Label(frame, text="Face Vote Precision", font="Arial 30 ", background="Light Blue")
label.place(x=50,y=20)

image=Image.open("lg.png_-removebg-preview.png")
image = image.resize((90,90))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo,background="Light blue")
logo_label.place(x=0,y=0)

cross_btn=Button(frame,text="x",bg="Light Blue",fg="Black",font="Candara 15 bold",border=0,command=move_to_cand_portal)
cross_btn.place(x=635,y=0)

margin_frame = Frame(root,width=1700,background="Black")  # Adjust the height 
margin_frame.place(y=95)

cand_lable=Label(root,text="Candidate Login",bg="white",fg="Black",font="Rockwell 22 bold")
cand_lable.place(x=267,y=105)

frame1=Frame(root,background="Light Blue",height=390,width=540)
frame1.place(x=82,y=150)
    
image=Image.open("log-removebg-preview.png")
image = image.resize((140,105))
photo1=ImageTk.PhotoImage(image)
logo_label1=Label(frame1,image=photo1,background="Light blue")
logo_label1.place(x=221,y=0)
    
username=Label(frame1,text="Voter ID  :- ",foreground="Black",background="Light Blue",fg="Black",font="Times 18 ",border=0)
username.place(x=90,y=120)
cand_username=Entry(frame1,foreground="Black",background="White",font="Times 14 ",border=0,bd=2,width=25)
cand_username.place(x=220,y=120)

password=Label(frame1,text="Password  :- ",foreground="Black",background="Light Blue",font="Times 18 ",border=0)
password.place(x=90,y=185)
cand_password=Entry(frame1,foreground="Black",background="White",font="Times 14 ",border=0,bd=2,show="*",width=25)
cand_password.place(x=220,y=185)

login= Button(frame1,text="Log In", foreground="White",background="Blue",font="Candara 16 bold",border=0,bd=2,command=Candidate_login)
login.place(x=240,y=260)

lable=Label(frame1,text="Not Registered ?",fg="Black",bg="Light Blue",font="Calibri 15",border=NO,)
lable.place(x=180,y=340)

regbtn=Button(frame1,text="Register",fg="Blue",bg="Light Blue",font="calibri 15 bold underline",border=0,cursor="hand2",command=move_to_cand_regentry)
regbtn.place(x=320,y=332)


root.mainloop()