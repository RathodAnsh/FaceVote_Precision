from tkinter import *
from tkinter import Tk
from subprocess import call
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import sys
import io
from tkinter import filedialog

if len(sys.argv) > 1:
    voter_id = sys.argv[1]
else:
    print("Error: Voter ID not provided.")
    sys.exit(1) 


def candidate_reg():
 # Connect to MySQL database
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ansh@7514",
        database="voter"
    )
        cursor = connection.cursor()
        select_query=("SELECT * FROM register_detail WHERE Voterid=%s")
        cursor.execute(select_query,(voter_id,))
        row=cursor.fetchone()
        
        if row:
            name_entry.insert(0, row[1])
            gender_entry.insert(0,row[3])  # Assuming you are using a RadioButton for gender
            age_entry.insert(0, row[4])
            dob_entry.insert(0, row[5])
            address_entry.insert(0, row[7])

            '''image_data = row[9]  # Assuming image is stored in the 9th column
            if image_data:
                image_stream = io.BytesIO(image_data)
                image = Image.open(image_stream)
                image = image.resize((168,187))  # Resize the image as needed
                photo = ImageTk.PhotoImage(image)
                fetch_img.config(image=photo)
                fetch_img.image = photo '''
        


    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")
            
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


def insert_candidate_data():

    party_name = party_entry.get()
    image_path = pic_path.get()
    user_image=pic_img.get()
    V_id=voterid_entry.get()

    if party_entry.get()=="" or pic_path.get()=="" or password_entry.get()=="":
         messagebox.showinfo('Result','Please provide complete details of the user') 
    else:     
        with open(image_path, 'rb') as file:
            image_detail = file.read()
        with open(user_image, 'rb') as file:
            user_image_data = file.read()    
        if voter_id==V_id:     
            try:
                # Connect to MySQL database
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Ansh@7514",
                    database="admin1"
                )
                
                cursor = connection.cursor()
                
                # Prepare the SQL INSERT query
                insert_query = ("INSERT INTO candidatereg "
                                "(Voter_id,Name, Gender, Age, Dob, Address, Party_name, P_image,password,voter_image) "
                                "VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s)")
                
                # Get the values from the tkinter Entry and Text widgets
                
                name = name_entry.get()
                gender = gender_entry.get()
                age = age_entry.get()
                dob = dob_entry.get()
                address = address_entry.get()
                password=password_entry.get()
                
                

                # Assuming the path to the party symbol image is stored
                
                # Execute the query with the values
                candidate_data = (V_id,name, gender, age, dob, address, party_name,image_detail,password,user_image_data)
                cursor.execute(insert_query, candidate_data)
                
                # Commit changes to the database
                connection.commit()
                
                # Show success message
                messagebox.showinfo("Success", "Candidate registration successful!")
                
            except mysql.connector.Error as error:
                messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")
                
            finally:
                if 'connection' in locals() and connection.is_connected():
                    cursor.close()
                    connection.close()
        else:
            messagebox.showerror("Error","Voterid not matched")

root=Tk()
root.geometry("800x780")

def Cand_regentry():
    root.destroy()
    call(["python","eCregentry.py"]) 

def move_to_cand_log():
    root.destroy()
    call(["python","eClogin.py"])    


frame=Frame(root,width=780,height=95,bg="Light Blue")
frame.place(x=40,y=0)
label=Label(frame, text="Face Vote Precision", font="Arial 30 ", background="Light Blue")
label.place(x=50,y=20)

backbtn=Button(frame,text="Back",bg="blue",fg="white",font="BerlinSans 15 bold",command=Cand_regentry)
backbtn.place(x=680,y=25)

image=Image.open("lg.png_-removebg-preview.png")
image = image.resize((90,90))
photo=ImageTk.PhotoImage(image)
logo_label=Label(image=photo,background="Light blue")
logo_label.place(x=0,y=0)

margin_frame = Frame(root,width=1700,height=4,background="Black")  # Adjust the height 
margin_frame.place(y=95)

frame1=Frame(root,width=800,height=650,bg="White")
frame1.place(y=96)

frame2=Frame(frame1,width=800,height=55,bg="Light Gray")
frame2.place(x=0,y=0)

pic_img=StringVar()
pic_img.set('')

def open_pic():
    path=askopenfilename()

    if path:
        img=ImageTk.PhotoImage(Image.open(path).resize((160,170)))
        pic_img.set(path)

        fetch_img.config(image=img)
        fetch_img.image=img



fetch_img=Button(frame1,text="Upload Image",background="Light Gray",font="Times 17",command=open_pic)
fetch_img.place(x=50,y=81,width=170,height=180)

lable1=Label(frame2,text="Registration",foreground="Black",background="Light Gray",font="Rockwell 22 bold",border=0)
lable1.place(x=327,y=5)

margin_frame = Frame(frame1,width=1700,height=1,background="Black")  # Adjust the height 
margin_frame.place(y=54)


pic_path=StringVar()
pic_path.set('')

def open_img():
    path=askopenfilename()

    if path:
        img1=ImageTk.PhotoImage(Image.open(path).resize((160,170)))
        pic_path.set(path)

        party_symbol.config(image=img1)
        party_symbol.image=img1

"""def pic_img_path():
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif")])
    if img_path:

        image = Image.open(img_path)
        image = image.resize((160,170))
        # Update the label text with the selected image path
        open_img.config(text="Selected Image Path: " + img_path)"""


party_symbol=Button(frame1,text="Upload\nParty Symbol",background="Light Gray",font="Times 17",command=open_img)
party_symbol.place(x=50,y=295,width=170,height=180)


margin_frameh2 = Frame(frame1,height=421,background="Black")  # Adjust the height 
margin_frameh2.place(x=253,y=70)
margin_frameb2 = Frame(frame1,width=233,background="Black")  # Adjust the height 
margin_frameb2.place(x=20,y=490)
margin_frameh1 = Frame(frame1,height=421,background="Black")  # Adjust the height 
margin_frameh1.place(x=20,y=70)
margin_frameb1 = Frame(frame1,width=233,background="Black")  # Adjust the height 
margin_frameb1.place(x=20,y=70)
margin_frameb3 = Frame(frame1,width=233,background="Black")  # Adjust the height 
margin_frameb3.place(x=20,y=280)


name=Label(frame1,text="Name :",font="Times 19",bg="White")
name.place(x=305,y=75)
name_entry=Entry(frame1,font="Times 19",bg="Light Gray",width=25)
name_entry.place(x=390,y=75)

"""partytype=Label(frame1,text="Type :",font="Times 19",bg="White")
partytype.place(x=305,y=130)
partyEntry1=Radiobutton(frame1,text='Independent',value='Independent',bg="White",font="times 18 ")
partyEntry1.place(x=390,y=127)
partyEntry2=Radiobutton(frame1,text='Non-Independent',value='Non-Independent',bg="White",font="times 18 ")
partyEntry2.place(x=550,y=127)"""


party_name=Label(frame1,text="Party Name :",font="Times 19",bg="White")
party_name.place(x=305,y=140)
party_entry=Entry(frame1,font="Times 19",bg="Light Gray",width=25)
party_entry.place(x=444,y=144)


gender=Label(frame1,text="Gender :",font="Times 19",bg="White")
gender.place(x=305,y=208)
gender_entry=Entry(frame1,font="Times 19",bg="Light Gray",width=25)
gender_entry.place(x=400,y=210)

age=Label(frame1,text="Age :",font="Times 19",bg="White")
age.place(x=305,y=278)
age_entry=Entry(frame1,font="Times 19",bg="Light Gray",width=25)
age_entry.place(x=368,y=280)

dob=Label(frame1,text="Date of Birth :",font="Times 19",bg="White")
dob.place(x=305,y=348)
dob_entry=Entry(frame1,font="Times 19",bg="Light Gray",width=25)
dob_entry.place(x=455,y=350)

voter_id_var = StringVar()
voter_id_var.set(voter_id)
voterid=Label(frame1,text="Voter Id :",font="Times 19",bg="White")
voterid.place(x=305,y=418)
voterid_entry=Entry(frame1,textvariable=voter_id_var,font="Times 18",bg="Light Gray")
voterid_entry.place(x=420,y=420)

address=Label(frame1,text="Address :",font="Times 18",bg="White")
address.place(x=30,y=540)
address_entry=Entry(frame1,font="Times 19",bg="Light Gray")
address_entry.place(x=135,y=540)

new_password=Label(frame1,text='''   Create password for login : 
    as candidate ''',font="Times 18",bg="White")
new_password.place(x=288,y=470)
password_entry=Entry(frame1,font="Times 19",bg="Light Gray",width=15,show="*")
password_entry.place(x=573,y=472)


#label= Label(frame1,text=" ---> Please confirm your details ", foreground="Red", font="Candara 20 ",border=0)
#label.place(x=150,y=650)

submit= Button(frame1,text="Submit", foreground="White",background="Blue",font="Candara 18 bold",border=0,command=insert_candidate_data)
submit.place(x=375,y=595)


candidate_reg()
root.mainloop()

