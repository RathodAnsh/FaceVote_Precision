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

def party_data():

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
            pname_label.config(text=row[6])

            image_symbol_data = row[7]  # Assuming image is stored in the 7th column
            if image_symbol_data:   
                image_symbol = io.BytesIO(image_symbol_data)
                image = Image.open(image_symbol)
                image = image.resize((168,187))  # Resize the image as needed
                photo1 = ImageTk.PhotoImage(image)
                party_symbol.config(image=photo1)
                party_symbol.image = photo1 
                

        

    
      
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")
            
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

#===================================Main Frame======================================
root=Tk()
root.geometry("650x500")

def move_to_castvote():
    root.destroy()
    

frame=Frame(root,width=780,height=95)
frame.place(x=40,y=0)
label=Label(frame, text="Candidate Details", font="Arial 30 bold")
label.place(x=160,y=20)

image=Image.open("profile-removebg-preview.png")
image = image.resize((80,80))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo)
logo_label.place(x=110,y=0)




margin_frame = Frame(root,width=1700,background="Black")  # Adjust the height 
margin_frame.place(y=95)

#==============================================New frame created============================================

frame1=Frame(root,width=800,height=560,bg="White")
frame1.place(y=96)


party_symbol=Label(frame1,text="Party Symbol ",background="Light Gray",font="Times 17")
party_symbol.place(x=40,y=70)


"""id=Label(frame1,text="Voter ID :",font="Times 19",bg="White")
id.place(x=30,y=370)
id=Label(frame1,font="Times 19",bg="Light Gray",width=15)
id.place(x=30,y=410)"""




name=Label(frame1,text="Name :",font="Times 19 bold",bg="White")
name.place(x=250,y=100)
name_label=Label(frame1,font="Times 19",bg="White")
name_label.place(x=335,y=100)

pname=Label(frame1,text="Party Name :",font="Times 19 bold",bg="White")
pname.place(x=250,y=170)
pname_label=Label(frame1,font="Times 19",bg="White")
pname_label.place(x=393,y=172)

back_btn=Button(frame1,text="Back",bg="Light Gray",font="BerlinSans 15 bold",command=move_to_castvote)
back_btn.place(x=550,y=340)

party_data()

root.mainloop()
