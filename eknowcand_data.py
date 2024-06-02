from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk
from subprocess import call
import sys
import mysql.connector
from tkinter import messagebox
import io
import os


if len(sys.argv) > 1:
    voter_id = sys.argv[1]
else:
    print("Error: Voter ID not provided.")
    sys.exit(1) 

#===========================================Fetching data from database into Label============================================

def candidate_profile():

    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ansh@7514",
        database="admin1"
    )
        cursor = connection.cursor()
        select_query=("SELECT * FROM Candidate_main WHERE Voter_id=%s")
        cursor.execute(select_query,(voter_id,))
        row=cursor.fetchone()
        
        if row:
            
            name_label.config(text=row[1])
            gender_label.config(text=row[2])
            age_label.config(text=row[3])
            #dob_label.config(text=row[6])
            address_label.config(text=row[5])
            pname_label.config(text=row[6])

            image_symbol_data = row[7]  # Assuming image is stored in the 8th column
            if image_symbol_data:   
                image_symbol = io.BytesIO(image_symbol_data)
                image = Image.open(image_symbol)
                image = image.resize((168,187))  # Resize the image as needed
                photo1 = ImageTk.PhotoImage(image)
                party_symbol.config(image=photo1)
                party_symbol.image = photo1 
                

            image_data = row[8]  # Assuming image is stored in the 8th column
            if image_data:
                image_stream = io.BytesIO(image_data)
                image = Image.open(image_stream)
                image = image.resize((168,187))  # Resize the image as needed
                photo2 = ImageTk.PhotoImage(image)
                image_label.config(image=photo2)
                image_label.image = photo2

    
      
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")
            
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

#===================================Main Frame======================================
root=Tk()
root.geometry("810x650")

def move_to_verify_cand():
    root.destroy()
    

frame=Frame(root,width=780,height=95)
frame.place(x=40,y=0)
label=Label(frame, text="Candidate Details", font="Arial 30 bold")
label.place(x=240,y=20)

image=Image.open("profile-removebg-preview.png")
image = image.resize((80,80))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo)
logo_label.place(x=190,y=0)

back_btn=Button(text="Back",bg="Light Gray",font="BerlinSans 15 bold",command=move_to_verify_cand)
back_btn.place(x=720,y=50)


margin_frame = Frame(root,width=1700,background="Black")  # Adjust the height 
margin_frame.place(y=95)

#==============================================New frame created============================================

frame1=Frame(root,width=800,height=560,bg="White")
frame1.place(y=96)

image_label=Label(frame1,text="Image",background="Light Gray",font="Times 17")
image_label.place(x=50,y=81)

party_symbol=Label(frame1,text="Party Symbol ",background="Light Gray",font="Times 17")
party_symbol.place(x=50,y=292)


"""id=Label(frame1,text="Voter ID :",font="Times 19",bg="White")
id.place(x=30,y=370)
id=Label(frame1,font="Times 19",bg="Light Gray",width=15)
id.place(x=30,y=410)"""

margin_frameh2 = Frame(frame1,height=421,background="Black")  # Adjust the height 
margin_frameh2.place(x=253,y=70)
margin_frameb2 = Frame(frame1,width=233,background="Black")  # Adjust the height 
margin_frameb2.place(x=20,y=490)
margin_frameh1 = Frame(frame1,height=421,background="Black")  # Adjust the height 
margin_frameh1.place(x=20,y=70)
margin_frameb1 = Frame(frame1,width=233,background="Black")  # Adjust the height 
margin_frameb1.place(x=20,y=70)
margin_frameb3 = Frame(frame1,width=233,background="Black")  # Adjust the height 
margin_frameb3.place(x=20,y=280)


name=Label(frame1,text="Name :",font="Times 19 bold",bg="White")
name.place(x=305,y=75)
name_label=Label(frame1,font="Times 19",bg="White")
name_label.place(x=390,y=75)


pname=Label(frame1,text="Party Name :",font="Times 19 bold",bg="White")
pname.place(x=305,y=140)
pname_label=Label(frame1,font="Times 19",bg="White")
pname_label.place(x=448,y=140)

gender=Label(frame1,text="Gender :",font="Times 19 bold",bg="White")
gender.place(x=305,y=205)
gender_label=Label(frame1,font="Times 19",bg="White")
gender_label.place(x=405,y=205)

age=Label(frame1,text="Age :",font="Times 19 bold",bg="White")
age.place(x=305,y=270)
age_label=Label(frame1,font="Times 19",bg="White")
age_label.place(x=368,y=270)

voterid=Label(frame1,text="Voter Id :",font="Times 19 bold",bg="White")
voterid.place(x=305,y=325)
voterid_label=Label(frame1,text=voter_id,font="Times 18",bg="White")
voterid_label.place(x=417,y=325)

address=Label(frame1,text="Address :",font="Times 18 bold",bg="White")
address.place(x=305,y=390)
address_label=Label(frame1,font="Times 19",bg="White")
address_label.place(x=417,y=388)




candidate_profile()

root.mainloop()

