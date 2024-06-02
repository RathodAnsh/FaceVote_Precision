from tkinter import *
from tkinter import Tk
import tkinter.messagebox as messagebox
from subprocess import call
from PIL import Image,ImageTk
import sys

if len(sys.argv) > 1:
    voter_id = sys.argv[1]
else:
    print("Error: Voter ID not provided.")
    sys.exit(1)  

root=Tk()
root.geometry("800x780")

def move_to_voter_log():
    confirm=messagebox.askyesno("Logout","Are you sure you want to logout")
    if confirm:
        root.destroy()
        call(['python', "eVlogin.py"])

def move_to_voter_profile():
    root.destroy()
    call(['python', "eVprofile.py",voter_id])

def move_to_know_candidate():
    root.destroy()
    call(['python', "eknowyourcandi.py",voter_id])

def move_to_voting():
    root.destroy()
    call(['python', "eVcast.py",voter_id])  

def move_to_result():
    root.destroy()
    call(['python', "eresult.py",voter_id]) 
               
    
def on_mousewheel(scroll):
    canvas.yview_scroll(int((scroll.delta / 120)), "units")

# Create a frame to contain the scrollable content
scroll_frame = Frame(root)

# Add a Canvas widget for scrolling
canvas = Canvas(scroll_frame, bg="White")
scrollbar = Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0,0),window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Bind mousewheel event to scroll
canvas.bind_all("<MouseWheel>", on_mousewheel)  

background_frame = Frame(root, bg="Light Blue")
background_frame.pack(fill=X)
label = Label(background_frame, text="Face Vote Precision", foreground="black", font="Arial 33 ", background="Light Blue")
label.pack(padx=(0, 150), pady=(28,25))

image=Image.open("lg.png_-removebg-preview.png")
image = image.resize((110,100))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo,background="Light blue")
logo_label.place(x=0,y=5)

margin_frame = Frame(root,width=1700,background="Black")  # Adjust the height 
margin_frame.place(y=110)

frame=Frame(scroll_frame)

lable=Label(frame,background="Light Gray",height=3,width=700)
lable.grid(row=0,column=0)

image=Image.open("profile-removebg-preview.png")
image = image.resize((40,40))
photo1=ImageTk.PhotoImage(image)
logo_label=Label(frame,image=photo1,background="Light gray")
logo_label.place(x=2,y=4)

profile=Button(frame,text=voter_id,background="Light Gray",fg="Black",font="calibri 15 bold",border=0,bd=0,command=move_to_voter_profile)
profile.place(x=50,y=8)

margin_frame = Frame(frame,height=55,background="Black",width=2)  # Adjust the height 
margin_frame.place(x=130,y=2)

image=Image.open("logout-removebg-preview.png")
image = image.resize((40,40))
photo2=ImageTk.PhotoImage(image)
logo_label=Label(frame,image=photo2,background="Light gray")
logo_label.place(x=680,y=4)

logout=Button(frame,text="Logout",background="Light Gray",fg="Black",font="calibri 15 bold",border=0,bd=0,height=1,width=6,command=move_to_voter_log)
logout.place(x=725,y=6)

margin_frame = Frame(frame,height=55,background="Black",width=2)  # Adjust the height 
margin_frame.place(x=675,y=2)

lable=Label(frame,text="Voter Portal",foreground="Black",bg="Light Gray",font="Rockwell 26 bold")
lable.place(x=315,y=3)

frame.pack()

buttons_frame = Frame(scrollable_frame)

image=Image.open("castvote-removebg-preview.png")
image = image.resize((220,160))
photo3=ImageTk.PhotoImage(image)
voter=Button(buttons_frame,image=photo3,background="Light blue",command=move_to_voting)
voter.grid(row=1,column=0,pady=(40,0))

image=Image.open("candi-removebg-preview.png")
image = image.resize((220,160))
photo4=ImageTk.PhotoImage(image)
voter=Button(buttons_frame,image=photo4,background="Light blue",command=move_to_know_candidate)
voter.grid(row=0,column=0,pady=(40,0))

image=Image.open("result-removebg-preview.png")
image = image.resize((220,160))
photo5=ImageTk.PhotoImage(image)
voter=Button(buttons_frame,image=photo5,background="Light blue",command=move_to_result  )
voter.grid(row=2,column=0,pady=(40,0))


buttons_frame.pack(padx=(170,600),pady=(0,50))

lable=Button(scrollable_frame,text="Cast Vote",foreground="Blue",font="Arial 18 underline ",bd=0,command=move_to_voting)
lable.place(x=470,y=310)

lable=Button(scrollable_frame,text="Know your candidate",foreground="Blue",font="Arial 18 underline ",bd=0,command=move_to_know_candidate)
lable.place(x=420,y=101)

lable=Button(scrollable_frame,text="Results",foreground="Blue",font="Arial 18 underline ",bd=0,command=move_to_result)
lable.place(x=480,y=515)

margin_frame = Frame(scrollable_frame,height=613,width=1,background="Black")  # Adjust the height 
margin_frame.place(x=130,y=25)
margin_frame = Frame(scrollable_frame,height=614,width=1,background="Black")  # Adjust the height 
margin_frame.place(x=675,y=25)
margin_frame = Frame(scrollable_frame,width=545,height=1,background="Black")  # Adjust the height 
margin_frame.place(x=130,y=25)
margin_frame = Frame(scrollable_frame,width=545,height=1,background="Black")  # Adjust the height 
margin_frame.place(x=130,y=225)
margin_frame = Frame(scrollable_frame,width=545,height=1,background="Black")  # Adjust the height 
margin_frame.place(x=130,y=432)
margin_frame = Frame(scrollable_frame,width=545,height=1,background="Black")  # Adjust the height 
margin_frame.place(x=130,y=638)

frame2=Frame(scrollable_frame)



frame2.pack(padx=(170,600),pady=(0,50))


canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

scroll_frame.pack(fill=BOTH, expand=True)

root.mainloop()