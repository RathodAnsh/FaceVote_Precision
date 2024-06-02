import cv2
from tkinter import *
from tkinter import Tk
from subprocess import call
from PIL import Image, ImageTk
# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Initialize the webcam
cap = cv2.VideoCapture(0)
scale_factor = 1

def update_lable():
    # Read the frame from the webcam
    ret,frame = cap.read()
    
    # Convert the frame to grayscale
    resized_frame = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces in the root
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
       cv2.rectangle(resized_frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    img = Image.fromarray(cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGBA))    
    img = ImageTk.PhotoImage(image=img)
    lable.img = img
    lable.config(image=img)
    lable.after(10, update_lable)
    # Display the root

root = Tk()

root.title("Face Recognition")

root.geometry("700x730")

def move_to_voter_detail():
    root.destroy()
    # Release the webcam and close all window
    cap.release()
    cv2.destroyAllWindows()
    call(['python', "eregdetails.py"])

def move_to_vote_register():
    root.destroy()
    cap.release()
    cv2.destroyAllWindows()
    call(['python', "eVregister.py"])    

image=Image.open("scan_face_back.jpg")
image = image.resize((700,730))
photo=ImageTk.PhotoImage(image)
logo_label=Label(root,image=photo,background="Light blue")
logo_label.place(x=0,y=0)

next_btn=Button(root,text="Next",font="Candara 14 bold",bg="Midnight Blue",relief="flat",fg="White",command=move_to_voter_detail)
next_btn.place(x=330,y=620,width=90)

cross_btn=Button(root,text="X",font="Candara 14 bold",bg="Midnight Blue",relief="flat",fg="White",command=move_to_vote_register)
cross_btn.place(x=670,y=3,width=30)


camera_frame=Frame(root,bg="Blue",bd=6,relief=GROOVE)
camera_frame.place(x=43,y=95)
# Create a label to display the webcam feed
lable = Label(camera_frame,bd=2,width=600,height=450)
lable.pack(side="top")

# Start updating the label with the latest frame
update_lable()

# Run the Tkinter event loop
root.mainloop()

    
    
 
    



