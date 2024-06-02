from tkinter import *
from tkinter import Tk
from subprocess import call
from PIL import Image,ImageTk

root=Tk()
root.geometry("800x780")

def move_to_voter():
    root.destroy()
    call(["python","eVoterportal.py"])

def move_to_cand_portal():
    root.destroy()
    call(["python","eCandidateportal.py"])

def move_to_admin_log():
    root.destroy()
    call(["python","eadminlog.py"])     

def move_to_election_manage():
    root.destroy()
    call(["python","emanagementlog.py"])   

        


#function on_mousewheel which contain the argument scroll
def on_mousewheel(scroll):
    #yview_scroll scroll the canvas vertically
    #scrolling amount is determined by scroll.delta/120
    canvas.yview_scroll(int((scroll.delta / 120)), "units")

# Create a frame to contain the scrollable content
scroll_frame = Frame(root)

# Add a Canvas widget for scrolling
canvas = Canvas(scroll_frame, bg="white")
#it creates the vertical scrollbar 
scrollbar = Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
#creats another frame inside canvas which contains the scrollabel contents
scrollable_frame = Frame(canvas)
# Bind a function to the <Configure> event of the scrollable frame.
# This function will be called when the size of the scrollable frame changes.
# Inside the function, the canvas is configured to update its scroll region .
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
#this crates the window at (0,0) int the north-west anchor
canvas.create_window((0,0),window=scrollable_frame, anchor="nw")
#this configur the canvas to use scrollbar 
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

lable=Label(root,text="आधुनिक मतदान, नए भारत का निर्माण",font=("Mangal", 21),foreground="Orange")
lable.pack(padx=(90,60),pady=(15,0))


buttons_frame = Frame(scrollable_frame)

image=Image.open("voter-removebg-preview.png")
image = image.resize((120,120))
photo1=ImageTk.PhotoImage(image)
voter=Button(buttons_frame,image=photo1,command=move_to_voter)
voter.place(x=180,y=53)

image=Image.open("candidate-removebg-preview.png")
image = image.resize((120,120))
photo2=ImageTk.PhotoImage(image)
voter=Button(buttons_frame,image=photo2,command=move_to_cand_portal)
voter.grid(row=0,column=1,padx=500,pady=(50,90))

image=Image.open("Emanage.png-removebg-preview.png")
image = image.resize((120,120))
photo3=ImageTk.PhotoImage(image)
voter=Button(buttons_frame,image=photo3,command=move_to_election_manage)
voter.place(x=180,y=268)

image=Image.open("admin-removebg-preview.png")
image = image.resize((120,120))
photo4=ImageTk.PhotoImage(image)
voter=Button(buttons_frame,image=photo4,command=move_to_admin_log)
voter.grid(row=1,column=1,pady=(0,70))

buttons_frame.pack()

lable=Label(scrollable_frame,text="Voter",foreground="Black",font="Arial 18 ")
lable.place(x=215,y=200)

lable=Label(scrollable_frame,text="Candidate",foreground="Black",font="Arial 18 ")
lable.place(x=505,y=200)

lable=Label(scrollable_frame,text="Election\nManagement",foreground="Black",font="Arial 18 ")
lable.place(x=177,y=416)

lable=Label(scrollable_frame,text="Admin",foreground="Black",font="Arial 18 ")
lable.place(x=525,y=416)

txt=Label(scrollable_frame,foreground="Black",font="times 20")
txt.pack()

about_us=Frame(scrollable_frame)

about_lable=Label(about_us,text="ABOUT US",font="Rockwell 24 bold underline")
about_lable.grid(row=0,column=0,pady=20)

txt=Label(about_us ,text="""FaceVote Precision is a groundbreaking 
electronic voting system focused on speed and accuracy.
We ensure that everyone's vote counts by using advanced
technology while maintaining high security standards. 
Our goal is to make voting easy and transparent for everyone, 
revolutionizing elections worldwide. Join us in shaping 
the future of democracy with FaceVote Precision.""",foreground="White",font="Candara 19",bg="Midnight Blue")
txt.grid(row=1,column=0)



about_us.pack(pady=(10,70),padx=75,side=LEFT)



canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

scroll_frame.pack(fill=BOTH, expand=True)


root.mainloop()