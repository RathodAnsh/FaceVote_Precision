from tkinter import *
from tkinter import Tk
from subprocess import call
from PIL import Image,ImageTk

root=Tk()
root.geometry("800x780")

def move_to_reg_entry():
    root.destroy()
    call(["python","eCregentry.py"])

def move_to_cand_log():
    root.destroy()
    call(["python","eClogin.py"])  

def move_to_dashboard():
    root.destroy()
    call(["python","edashboard.py"])      


background_frame = Frame(root, bg="Light Blue")
background_frame.pack(fill=X)
label = Label(background_frame, text="Face Vote Precision", foreground="black", font="Arial 33 ", background="Light Blue")
label.pack(padx=(0, 150), pady=(28,25))

image=Image.open("lg.png_-removebg-preview.png")
image = image.resize((110,100))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo,background="Light blue")
logo_label.place(x=0,y=5)

backbtn=Button(text="Back",bg="blue",fg="white",font="BerlinSans 15 bold",command=move_to_dashboard)
backbtn.place(x=720,y=33)

margin_frame = Frame(root,width=1700,background="Black")  # Adjust the height 
margin_frame.place(y=110)

lable=Label(root,text="Candidate Portal",foreground="Black",font="Rockwell 28 bold")
lable.pack(pady=(15,0))

image=Image.open("cand_img-removebg-preview.png")
image = image.resize((700,410))
photo1=ImageTk.PhotoImage(image)
logo_label=Label(image=photo1)
logo_label.place(x=50,y=190)

regbtn=Button(root,text="Register",bg="blue",fg="white",font="BerlinSans 18 bold",command=move_to_reg_entry)
regbtn.place(x=350,y=620)

lable=Label(root,text="Already rigisterd ?",fg="Black",font="Calibri 15",border=NO)
lable.place(x=310,y=700)

logbtn=Button(root,text="Login",fg="Blue",font="calibri 17 bold underline",border=0,cursor="hand2",command=move_to_cand_log)
logbtn.place(x=463,y=688)

root.mainloop()