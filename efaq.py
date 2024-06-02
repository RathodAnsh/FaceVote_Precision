from tkinter import *
from tkinter import Tk
from subprocess import call
from PIL import Image,ImageTk

root=Tk()
root.geometry("800x780")

def move_to_main_vote():
    root.destroy()
    call(['python', "edashboard.py"])
    
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

backbtn=Button(text="Back",bg="blue",fg="white",font="BerlinSans 15 bold",command=move_to_main_vote)
backbtn.place(x=720,y=33)

margin_frame = Frame(root,width=1700,background="Black")  # Adjust the height 
margin_frame.place(y=110)

frame=Frame(scroll_frame)



canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

scroll_frame.pack(fill=BOTH, expand=True)

root.mainloop()