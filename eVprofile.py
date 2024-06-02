from tkinter import *
from tkinter import Tk
from PIL import Image,ImageTk
from subprocess import call
import sys
import mysql.connector
from tkinter import messagebox
import io

if len(sys.argv) > 1:
    voter_id = sys.argv[1]
else:
    print("Error: Voter ID not provided.")
    sys.exit(1) 

def fetch_detail():

    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ansh@7514",
        database="voter"
    )
        cursor = connection.cursor()
        select_query=("SELECT * FROM register_detail WHERE Voterid=%s")
        cursor.execute(select_query,(voter_id,))
        row=cursor.fetchone()
        
        if row:
            
            name_label.config(text=row[1])
            fname_label.config(text=row[2])
            gender_label.config(text=row[3])
            age_label.config(text=row[4])
            #dob_label.config(text=row[6])
            #issue_date_label.config(text=row[7])
            address_label.config(text=row[7])

            image_data = row[8]  # Assuming image is stored in the 8th column
            if image_data:
                image_stream = io.BytesIO(image_data)
                image = Image.open(image_stream)
                image = image.resize((210,260))  # Resize the image as needed
                photo = ImageTk.PhotoImage(image)
                img_lable.config(image=photo)
                img_lable.image = photo 

    
      
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")
            
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

root=Tk()
root.geometry("790x600")

def move_to_main_vote():
    root.destroy()
    call(['python', "eVote.py",voter_id])

frame=Frame(root,width=780,height=95,bg="Light Blue")
frame.place(x=40,y=0)
label=Label(frame, text="Profile", font="Arial 34 bold", background="Light Blue")
label.place(x=70,y=20)

image=Image.open("profile-removebg-preview.png")
image = image.resize((85,90))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo,background="Light blue")
logo_label.place(x=0,y=0)

back=Button(text="Back",bg="blue",fg="white",font="BerlinSans 15 bold",command=move_to_main_vote)
back.place(x=700,y=30)

margin_frame = Frame(root,width=1700,background="Black")  # Adjust the height 
margin_frame.place(y=95)

img_lable=Label(root,text="Image",background="Light Gray",font="Times 17")
img_lable.place(x=15,y=125)

id=Label(root,text="Voter ID :",font="Times 19 bold")
id.place(x=15,y=415)
id_lable=Label(root,text=voter_id,font="Times 19")
id_lable.place(x=128,y=415)

margin_frame = Frame(root,height=366,background="Black")  # Adjust the height 
margin_frame.place(x=238,y=118)
margin_frame = Frame(root,width=233,background="Black")  # Adjust the height 
margin_frame.place(x=5,y=483)
margin_frame = Frame(root,height=366,background="Black")  # Adjust the height 
margin_frame.place(x=5,y=118)
margin_frame = Frame(root,width=233,background="Black")  # Adjust the height 
margin_frame.place(x=5,y=118)

name=Label(root,text="Name :",font="Times 19 bold")
name.place(x=290,y=140)
name_label=Label(root,font="Times 19")
name_label.place(x=375,y=140)

fname=Label(root,text="Father's Name :",font="Times 19 bold")
fname.place(x=290,y=200)
fname_label=Label(root,font="Times 19")
fname_label.place(x=470,y=200)

gender=Label(root,text="Gender :",font="Times 19 bold")
gender.place(x=290,y=260)
gender_label=Label(root,font="Times 19")
gender_label.place(x=390,y=260)

age=Label(root,text="Age :",font="Times 19 bold")
age.place(x=290,y=320)
age_label=Label(root,font="Times 19")
age_label.place(x=350,y=320)

'''dob=Label(root,text="Date of Birth :",font="Times 19")
dob.place(x=290,y=380)
dob_label=Label(root,font="Times 19")
dob_label.place(x=500,y=380)

issue_date=Label(root,text="Issued Date :",font="Times 19")
issue_date.place(x=290,y=440)
issue_date_label=Label(root,font="Times 19")
issue_date_label.place(x=480,y=440)'''

address=Label(root,text="Address :",font="Times 19 bold")
address.place(x=290,y=380)
address_label=Label(root,font="Times 19")
address_label.place(x=405,y=380)



#label= Button(root,text="Change Password", foreground="Blue",font="Candara 18 bold",bd=0)
#label.place(x=320,y=635)
fetch_detail()
root.mainloop()

