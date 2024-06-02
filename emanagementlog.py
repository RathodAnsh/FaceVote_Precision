from tkinter import *
from tkinter import Tk
from subprocess import call
import tkinter.messagebox as messagebox
from PIL import Image,ImageTk

root=Tk()
root.geometry("700x600")

def move_to_dashboard():
    root.destroy()
    call(["python","edashboard.py"])     


frame=Frame(root,width=700,height=95,bg="Light Blue")
frame.place(x=40,y=0)
label=Label(frame, text="Face Vote Precision", font="Arial 30 ", background="Light Blue")
label.place(x=50,y=20)

image=Image.open("lg.png_-removebg-preview.png")
image = image.resize((90,90))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo,background="Light blue")
logo_label.place(x=0,y=0)

cross_btn=Button(frame,text="x",bg="Light Blue",fg="Black",font="Candara 15 bold",border=0,command=move_to_dashboard)
cross_btn.place(x=635,y=0)

margin_frame = Frame(root,width=1700,background="Black")  # Adjust the height 
margin_frame.place(y=95)

admin_lable=Label(root,text="Election Management\nLogin",fg="Black",font="Rockwell 22 bold")
admin_lable.place(x=210,y=97)

frame1=Frame(root,background="Light Blue",height=350,width=540)
frame1.place(x=82,y=180)

image=Image.open("adminlog-removebg-preview.png")
image = image.resize((125,110))
photo1=ImageTk.PhotoImage(image)
logo_label=Label(frame1,image=photo1,background="Light blue")
logo_label.place(x=221,y=0)


username=Label(frame1,text="Username :- ",foreground="Black",background="Light Blue",fg="Black",font="Times 18 ",border=0)
username.place(x=90,y=120)
username1=Entry(frame1,foreground="Black",background="White",font="Times 14 ",border=0,bd=2,width=25)
username1.place(x=220,y=120)

password=Label(frame1,text="Password  :- ",foreground="Black",background="Light Blue",font="Times 18 ",border=0)
password.place(x=90,y=185)
password1=Entry(frame1,foreground="Black",background="White",font="Times 14 ",border=0,bd=2,show="*",width=25)
password1.place(x=220,y=185)

username=StringVar()

def manage_log():
    username=username1.get()
    password=password1.get()
    if username=="Election" and password=="123456":
       messagebox.showinfo("Login Successful","Login Successful!")
       root.destroy()
       call(["python","eElectionmanage.py"]) 
    if username=="" or password=="":
       messagebox.showwarning("no entry","Please enter Username or Password")
    elif username!="Election" or password!="123456":
       messagebox.showerror("invalid entry","Invalid Username or Password")    
   
log= Button(frame1,text="Log In", foreground="White",background="Blue",font="Candara 16 bold",border=0,bd=2,command=manage_log)
log.place(x=240,y=260)    


root.mainloop()