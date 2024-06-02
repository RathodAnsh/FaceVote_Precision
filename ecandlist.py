from tkinter import *
from tkinter import Tk
import tkinter.messagebox as messagebox
from subprocess import call
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector


root=Tk()
root.geometry("800x703")

def move_to_admin_dash():
      root.destroy()
      call(["python","eElectionmanage.py"])


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

admin_label=Label(frame2,text="Candidate list",font="Rockwell 24  ",bg="Light Gray",bd=0)
admin_label.place(x=40,y=7)

image=Image.open("logout-removebg-preview.png")
image = image.resize((40,40))
photo2=ImageTk.PhotoImage(image)
logo_label=Label(frame2,image=photo2,background="Light gray")
logo_label.place(x=675,y=4)

Cand_logout=Button(frame2,text="Back",background="Light Gray",fg="Black",font="calibri 15 bold",border=0,bd=0,height=1,width=6,command=move_to_admin_dash)
Cand_logout.place(x=720,y=6)

last_frame=Frame(root,bg="Gray")
last_frame.place(y=162,height=540,width=800)

style = ttk.Style()
style.configure("Treeview", font=("Arial", 11)) 
style.configure("Treeview.Heading", font=("Arial 13 bold"))

table_frame=Frame(last_frame,highlightbackground="Black",highlightthickness=2,bg="white",bd=7,relief=GROOVE)
table_frame.pack(fill=BOTH,expand=True)


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

fetch_main_candidate_data()            

root.mainloop()