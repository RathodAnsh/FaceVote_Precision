from tkinter import *
from tkinter import Tk
from subprocess import call
from PIL import Image,ImageTk

root=Tk()
root.geometry("600x500")

frame=Frame(root,width=700,height=95,bg="Light Blue")
frame.place(x=40,y=0)
label=Label(frame, text="Face Vote Precision", font="Arial 30 ", background="Light Blue")
label.place(x=50,y=20)

image=Image.open("lg.png_-removebg-preview.png")
image = image.resize((90,90))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo,background="Light blue")
logo_label.place(x=0,y=0)

margin_frame = Frame(root,width=1700,background="Black")  # Adjust the height 
margin_frame.place(y=95)

lable=Label(root,text="Please Scan your face to confirm it is you",foreground="Black",font="serbian 22 underline ")
lable.pack(pady=(130,0))

label1= Button(root, text="Scan Your face", foreground="Blue", font="Rockwell 33 ", background="Light Gray",border=0,cursor="hand2")
label1.place(x=185,y=260)

image=Image.open("camera-removebg-preview.png")
image = image.resize((110,82))
photo1=ImageTk.PhotoImage(image)
logo_label=Label(image=photo1,border=NO,background="Light Gray")
logo_label.place(x=85,y=260)

backbtn1=Button(root,text="Back",bg="blue",fg="white",font="BerlinSans 15 bold")
backbtn1.place(x=505,y=430)

root.mainloop()