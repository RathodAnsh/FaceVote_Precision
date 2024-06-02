from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from subprocess import call
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk
from tkinter import ttk

root=Tk()
root.geometry("800x780")

def move_to_admin_dash():
      root.destroy()
      call(["python","eAdmindash.py"])

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

admin_label=Label(frame2,text="Add  Voters",font="Rockwell 24  ",bg="Light Gray",bd=0)
admin_label.place(x=30,y=7)

image=Image.open("logout-removebg-preview.png")
image = image.resize((40,40))
photo2=ImageTk.PhotoImage(image)
logo_label=Label(frame2,image=photo2,background="Light gray")
logo_label.place(x=675,y=4)

Cand_logout=Button(frame2,text="Back",background="Light Gray",fg="Black",font="calibri 15 bold",border=0,bd=0,height=1,width=6,command=move_to_admin_dash)
Cand_logout.place(x=720,y=6)

last_frame=Frame(root,bg="Gray")
last_frame.place(y=162,height=540,width=800)

table_frame=Frame(last_frame,highlightbackground="Black",highlightthickness=2,bg="white",bd=7,relief=GROOVE)
table_frame.pack(fill=BOTH,expand=True)


y_scroll=Scrollbar(table_frame,orient=VERTICAL)
x_scroll=Scrollbar(table_frame,orient=HORIZONTAL)

table=ttk.Treeview(table_frame,columns=("voter_id","name","gender","age"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set,height=50)

y_scroll.config(command=table.yview)
x_scroll.config(command=table.xview)
y_scroll.pack(side=RIGHT,fill=Y)
x_scroll.pack(side=BOTTOM,fill=X)

table.heading("voter_id",text="Voter Id")
table.heading("name",text="Name")
table.heading("gender",text="Gender")
table.heading("age",text="Age")

table['show']='headings'

table.column("voter_id",width=200)
table.column("name",width=350)
table.column("gender",width=130)
table.column("age",width=80)


table.pack(fill=BOTH,expand=True)

verify_cand=Button(root,text="Add",bd=2,bg="Light Green",fg="Black",font="cooper 15 bold")
verify_cand.place(x=350,y=720,height=40,width=120)

root.mainloop()