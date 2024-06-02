import cv2
from tkinter import *
from tkinter import Tk
from subprocess import call
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import sys
import os
import numpy as np
    
if len(sys.argv) > 1:
    voter_id = sys.argv[1]
    
else:
    print("Error: Voter ID not provided.")
    sys.exit(1)

root=Tk()
root.geometry("800x780")

def move_to_voter():
    root.destroy()
    call(['python', "eVoterportal.py"])

def move_to_scan():
    root.destroy()
    call(['python', "escanface.py"])    
   

background_frame = Frame(root, bg="Light Blue")
background_frame.pack(fill=X)
label = Label(background_frame, text="Face Vote Precision", foreground="black", font="Arial 33 ", background="Light Blue")
label.pack(padx=(0, 150), pady=(28,25))

image=Image.open("lg.png_-removebg-preview.png")
image = image.resize((110,100))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo,background="Light blue")
logo_label.place(x=0,y=5)

backbtn=Button(text="Back",bg="blue",fg="white",font="BerlinSans 15 bold",command=move_to_voter)
backbtn.place(x=720,y=33)

margin_frame = Frame(root,width=1700,background="Black")  # Adjust the height 
margin_frame.place(y=110)

lable=Label(root,text="Register Here !!",foreground="Black",font="Rockwell 28 bold")
lable.pack(pady=(15,0))

lable=Label(root,text='''  For Face Detection first generate your dataset & 
    then train your dataset''',foreground="Black",font="serbian 24 ")
lable.pack(pady=(40,0))

v_id=Label(root,text="Voter Id :-",font=("Arial",20))
v_id.place(x=260,y=370)
id_entry=Entry(root,width=14,bd=2,font="Arial 18")
id_entry.place(x=390,y=374,height=35)

id_entry.insert(0, voter_id)

name_voter=Label(root,text="Name :-",font=("Arial",20))
name_voter.place(x=260,y=440)
n_entry=Entry(root,width=14,bd=2,font="Arial 18")
n_entry.place(x=390,y=440,height=35)

label= Label(root,text="""Note : 'To Cast your Vote it is mandatory to generate 
             and train dataset of your face'""", foreground="Red", font="Candara 20 ",border=NO)
label.place(x=50,y=620)
#scan_btn= Button(root, text="Scan Your face", foreground="Blue", font="Rockwell 33 ", background="Light Gray",border=0,cursor="hand2",command=move_to_scan)
#scan_btn.place(x=290,y=350)
def generate_dataset():
    ids=id_entry.get()
    name=n_entry.get()

    if not ids or not name :
        messagebox.showinfo('Result','All fields are required') 


    else:
        try:
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ansh@7514",
            database="admin1"
            )
            mycursor=connection.cursor()
            mycursor.execute("SELECT * from face_data ")
            '''existing_data = mycursor.fetchall()
            if existing_data:
                messagebox.showinfo('Result',f'Data for voterid {id_entry.get()} is already generated!')
            else:'''
            myresult=mycursor.fetchall()
            id=1
            for x in myresult:
                id+=1
            sql="INSERT INTO face_data(id,Voterid,Name) VALUES (%s,%s,%s)"
            val=(id,id_entry.get(),n_entry.get())
            mycursor.execute(sql,val)
            connection.commit()
            
            face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            def face_cropped(img):
            
                gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray,1.3,5)
                #scaling factor=1.3
                #Minimum neighbor = 5

                if faces is ():
                    return None
                for(x,y,w,h) in faces:
                    cropped_face=img[y:y+h,x:x+w]
                    return cropped_face

            
            
            cap = cv2.VideoCapture(0)
            img_id=0

            while True:
                ret,frame = cap.read()
                if face_cropped(frame) is not None:
                    img_id+=1
                    face = cv2.resize(face_cropped(frame),(450,450))
                    face  = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1, (0,255,0),2)
                    # (50,50) is the origin point from where text is to be written
                    # font scale=1
                    #thickness=2

                    cv2.imshow("Cropped face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==200:
                        break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo('Result','Generating dataset completed!!!')

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")
                
        finally:
            if 'connection' in locals() and connection.is_connected():
                mycursor.close()
                connection.close()
         

scan_btn= Button(root, text="Generate Data set", foreground="Blue", font="Rockwell 20 ", background="Light Gray",border=0,cursor="hand2",command=generate_dataset)
scan_btn.place(x=180,y=520)



def train_classifier():
    data_dir = "C:/Users/admin/Documents/e-voting/data"  # Use raw string to avoid escape sequence warning
    path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
    faces = []
    ids = []

    for image in path:
        img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        imageNp = np.array(img, 'uint8')
        id = int(os.path.split(image)[1].split(".")[1])

        faces.append(imageNp)
        ids.append(id)
        #cv2.imshow("Training", imageNp)
        #cv2.waitKey(1)  # Changed from '==13' to '1' for proper waitKey behavior

    ids = np.array(ids)

    # Train the classifier and save
    clf = cv2.face.LBPHFaceRecognizer_create()  # Use appropriate function for LBPH Face Recognizer creation
    clf.train(faces, ids)
    clf.write("classifier.xml")
    cv2.destroyAllWindows()
    
    messagebox.showinfo('Result', 'Training dataset completed!!!')  # Using messagebox from tkinter

     

train_btn= Button(root, text="Train data", foreground="Blue", font="Rockwell 20 ", background="Light Gray",border=0,cursor="hand2",command=train_classifier)
train_btn.place(x=490,y=520)

'''image=Image.open("camera-removebg-preview.png")
image = image.resize((110,82))
photo1=ImageTk.PhotoImage(image)
logo_label=Label(image=photo1,border=NO,background="Light Gray")
logo_label.place(x=180,y=350)'''

#label= Label(root,text="""Note : ' To initiate the voter registration process,it is mandatory to
        #      undergo facial scanning to authenticate the user's identity.'""", foreground="Red", font="Candara 20 ",border=NO)
#label.place(x=10,y=550)



root.mainloop()





