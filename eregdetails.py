from tkinter import *
from tkinter import Tk
from subprocess import call
from PIL import Image,ImageTk
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
            
            name_entry.insert(0, row[1])
            fname_entry.insert(0, row[2])
            gender_entry.insert(0,row[3])  # Assuming you are using a RadioButton for gender
            age_entry.insert(0, row[4])
            dob_entry.insert(0, row[5])
            issue_date_entry.insert(0, row[6])
            address_text.insert('1.0', row[7])

            image_data = row[8]  # Assuming image is stored in the 8th column
            if image_data:
                image_stream = io.BytesIO(image_data)
                image = Image.open(image_stream)
                image = image.resize((210,260))  # Resize the image as needed
                photo = ImageTk.PhotoImage(image)
                img_fetch.config(image=photo)
                img_fetch.image = photo 

    
      
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")
            
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
root=Tk()
root.geometry("800x780")

def move_to_generate():
    root.destroy()
    call(['python', "eVregister.py",voter_id])

    

background_frame = Frame(root, bg="Light Blue")
background_frame.pack(fill=X)
label = Label(background_frame, text="Face Vote Precision", foreground="black", font="Arial 33 ", background="Light Blue")
label.pack(padx=(0, 150), pady=(28,25))

image=Image.open("lg.png_-removebg-preview.png")
image = image.resize((110,100))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo,background="Light blue")
logo_label.place(x=0,y=5)

backbtn=Button(text="Back",bg="blue",fg="white",font="BerlinSans 15 bold")
backbtn.place(x=720,y=33)

margin_frame = Frame(root,width=1700,background="Black")  # Adjust the height 
margin_frame.place(y=110)

entry_frame=Frame(root,width=800,height=650,bg="White")
entry_frame.place(y=115)

img_fetch=Label(entry_frame,text="Image",background="Light Gray",font="Times 17")
img_fetch.place(x=15,y=25)

id=Label(entry_frame,text="Voter ID :",font="Times 19",bg="White")
id.place(x=15,y=300)
id=Label(entry_frame,text=voter_id,font="Times 19",bg="Light Gray",width=15)
id.place(x=15,y=340)

margin_frame = Frame(entry_frame,height=366,background="Black")  # Adjust the height 
margin_frame.place(x=238,y=18)
margin_frame = Frame(entry_frame,width=233,background="Black")  # Adjust the height 
margin_frame.place(x=5,y=383)
margin_frame = Frame(entry_frame,height=366,background="Black")  # Adjust the height 
margin_frame.place(x=5,y=18)
margin_frame = Frame(entry_frame,width=233,background="Black")  # Adjust the height 
margin_frame.place(x=5,y=18)

name=Label(entry_frame,text="Name :",font="Times 19",bg="White")
name.place(x=290,y=40)
name_entry=Entry(entry_frame,font="Times 19",bg="Light Gray",width=25)
name_entry.place(x=370,y=40)

fname=Label(entry_frame,text="Father's Name :",font="Times 19",bg="White")
fname.place(x=290,y=100)
fname_entry=Entry(entry_frame,font="Times 19",bg="Light Gray",width=25)
fname_entry.place(x=455,y=100)

gender=Label(entry_frame,text="Gender :",font="Times 19",bg="White")
gender.place(x=290,y=160)
gender_entry=Entry(entry_frame,font="Times 19",bg="Light Gray",width=25)
gender_entry.place(x=385,y=160)

age=Label(entry_frame,text="Age :",font="Times 19",bg="White")
age.place(x=290,y=220)
age_entry=Entry(entry_frame,font="Times 19",bg="Light Gray",width=25)
age_entry.place(x=353,y=220)

dob=Label(entry_frame,text="Date of Birth :",font="Times 19",bg="White")
dob.place(x=290,y=280)
dob_entry=Entry(entry_frame,font="Times 19",bg="Light Gray",width=25)
dob_entry.place(x=440,y=280)

issue_date=Label(entry_frame,text="Issued Date :",font="Times 19",bg="White")
issue_date.place(x=290,y=340)
issue_date_entry=Entry(entry_frame,font="Times 19",bg="Light Gray",width=25)
issue_date_entry.place(x=427,y=340)

address=Label(entry_frame,text="Address :",font="Times 19",bg="White")
address.place(x=15,y=420)
address_text=Text(entry_frame,font="Times 19",bg="Light Gray",width=50,height=2)
address_text.place(x=120,y=420)

label= Label(entry_frame,text=" ---> Please confirm your details ", foreground="Red", font="Candara 20 ",border=0,bg="White")
label.place(x=150,y=550)

next_btn= Button(entry_frame,text="NEXT", foreground="White",background="Blue",font="Candara 18 bold",border=0,command=move_to_generate)
next_btn.place(x=515,y=545)

#fetch_btn= Button(entry_frame,text="Show details", foreground="White",background="Blue",font="Candara 18 bold",border=0,command=fetch_detail)
#fetch_btn.place(x=515,y=575)
fetch_detail()
root.mainloop()

