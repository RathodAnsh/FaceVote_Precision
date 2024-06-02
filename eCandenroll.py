from tkinter import *
from tkinter import Tk
from subprocess import call
import tkinter.messagebox as messagebox
from PIL import Image,ImageTk
import sys
import mysql.connector
from tkinter import messagebox

if len(sys.argv) > 1:
    voter_id = sys.argv[1]
else:
    print("Error: Voter ID not provided.")
    sys.exit(1) 


def candidate_enrollment():
    
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ansh@7514",
        database="admin1"
    )
        cursor = connection.cursor()
        select_query="SELECT Voter_id,Name,Gender,Age,Dob,Address,Party_name,P_image,voter_image FROM candidatereg WHERE Voter_id=%s"
        cursor.execute(select_query,(voter_id,))
        candidate_data=cursor.fetchone()

        if candidate_data:
            insert_query="INSERT INTO candidatever (Voter_id, Name, Gender, Age, Dob, Address, Party_name,P_image,C_image) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s)"
            cursor.execute(insert_query,candidate_data)
            
            insert_id_query = "INSERT INTO enrolled_once (Voter_id) VALUES (%s)"
            cursor.execute(insert_id_query, (voter_id,))


        connection.commit()
        connection.close()
        confirm=messagebox.askyesno("Logout","Are you sure you want to Enroll")
        if confirm:
            messagebox.showinfo("enroll","Successfully enrolled")
        

    except mysql.connector.Error as error:
        messagebox.showerror("Error","You have already enrolled")
            
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            
root=Tk()
root.geometry("700x500")

def Cand_log():
    confirm=messagebox.askyesno("Logout","Are you sure you want to logout")
    if confirm:    
        root.destroy()
        call(["python","eClogin.py"])

def move_to_cand_profile():
        root.destroy()
        call(["python","eCprofile.py",voter_id])         


frame=Frame(root,width=700,height=95,bg="Light Blue")
frame.place(x=40,y=0)
label=Label(frame, text="Face Vote Precision", font="Arial 30 ", background="Light Blue")
label.place(x=50,y=20)

image=Image.open("lg.png_-removebg-preview.png")
image = image.resize((90,92))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo,background="Light blue")
logo_label.place(x=0,y=0)

margin_frame = Frame(root,width=1700,background="Black")  # Adjust the height 
margin_frame.place(y=95)

frame=Frame(root,background="Light Gray",height=50,width=700)
frame.place(y=95)



image=Image.open("profile-removebg-preview.png")
image = image.resize((40,40))
photo1=ImageTk.PhotoImage(image)
logo_label=Label(frame,image=photo1,background="Light gray")
logo_label.place(x=2,y=4)

profile=Button(frame,text=voter_id,background="Light Gray",fg="Black",font="calibri 15 bold",border=0,bd=0,command=move_to_cand_profile)
profile.place(x=50,y=8)

margin_frame = Frame(frame,height=55,background="Black",width=2)  # Adjust the height 
margin_frame.place(x=130,y=2)

image=Image.open("logout-removebg-preview.png")
image = image.resize((40,40))
photo2=ImageTk.PhotoImage(image)
logo_label=Label(frame,image=photo2,background="Light gray")
logo_label.place(x=575,y=4)

logout=Button(frame,text="Logout",background="Light Gray",fg="Black",font="calibri 15 bold",border=0,bd=0,height=1,width=6,command=Cand_log)
logout.place(x=620,y=6)

margin_frame = Frame(frame,height=55,background="Black",width=2)  # Adjust the height 
margin_frame.place(x=575,y=2)

enroll_frame=Frame(root,highlightbackground="Blue",highlightthickness=3)
enroll_frame.pack(padx=(20,0),pady=(240,0))
enroll_frame.configure(width=490,height=130)

lable_enroll=Label(root,text="Enroll yourself for election",font="Arial 20 ")
lable_enroll.place(x=190,y=270)



enroll_btn=Button(root,text="Enroll",bg="Green",fg="White",font="BerlinSans 14 bold",command=candidate_enrollment)
enroll_btn.place(x=330,y=320)



root.mainloop()