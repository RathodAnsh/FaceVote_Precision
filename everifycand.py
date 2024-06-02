from tkinter import *
from tkinter import Tk
import tkinter.messagebox as messagebox
from subprocess import call
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector



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

admin_label=Label(frame2,text="Candidate Verification",font="Rockwell 24  ",bg="Light Gray",bd=0)
admin_label.place(x=40,y=7)

image=Image.open("logout-removebg-preview.png")
image = image.resize((40,40))
photo2=ImageTk.PhotoImage(image)
logo_label=Label(frame2,image=photo2,background="Light gray")
logo_label.place(x=675,y=4)

back_btn=Button(frame2,text="Back",background="Light Gray",fg="Black",font="calibri 15 bold",border=0,bd=0,height=1,width=6,command=move_to_admin_dash)
back_btn.place(x=720,y=6)

#=====================================Creating new Frame for Treeview==========================================

last_frame=Frame(root,bg="Gray")
last_frame.place(y=162,height=540,width=800)

style = ttk.Style()
style.configure("Treeview", font=("Arial", 11)) 
style.configure("Treeview.Heading", font=("Arial 13 bold"))


table_frame=Frame(last_frame,highlightbackground="Black",highlightthickness=2,bg="white",bd=7,relief=GROOVE)
table_frame.pack(fill=BOTH,expand=True)


y_scroll=Scrollbar(table_frame,orient=VERTICAL)
x_scroll=Scrollbar(table_frame,orient=HORIZONTAL)
 

cand_table=ttk.Treeview(table_frame,columns=("voter_id","name","gender","age","dob","p_name"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set,height=50)

y_scroll.config(command=cand_table.yview)
x_scroll.config(command=cand_table.xview)
y_scroll.pack(side=RIGHT,fill=Y)
x_scroll.pack(side=BOTTOM,fill=X)

cand_table.heading("voter_id",text="Voter Id")
cand_table.heading("name",text="Name")
cand_table.heading("gender",text="Gender")
cand_table.heading("age",text="Age")
cand_table.heading("dob",text="Date of Birth")
cand_table.heading("p_name",text="Party Name")


cand_table['show']='headings'

cand_table.column("voter_id",width=120)
cand_table.column("name",width=250)
cand_table.column("gender",width=100)
cand_table.column("age",width=50)
cand_table.column("dob",width=150)
cand_table.column("p_name",width=250)


cand_table.pack(fill=BOTH,expand=True)

#==============Fetching data into table================================
def fetch_data_table():
      try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ansh@7514",
        database="admin1"
    )
        cursor = connection.cursor()
        cursor.execute("Select Voter_id,Name,Gender,Age,Dob,Address,Party_name from candidatever")
        data=cursor.fetchall()

        if len(data)!=0:
             cand_table.delete(*cand_table.get_children())
             for row in data:

                  cand_table.insert("",END,values=(row[0], row[1], row[2], row[3], row[4], row[6]))
             connection.commit()
        connection.close()     

      except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")
            
      finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

refresh_btn=Button(frame,text="Refresh",background="Light Gray",fg="Black",font="calibri 12 bold",border=0,bd=2,height=1,width=7,command=fetch_data_table)
refresh_btn.place(x=680,y=50)

#=========================Selecting row and passing voterid==============================================

def view_selected_row():
    selected_item = cand_table.focus()
    if selected_item:
        selected_row = cand_table.item(selected_item, 'values')
        voter_id = selected_row[0]  # Get the voter ID from the selected row
      
        call(['python', 'eviewprofile.py', voter_id])
    else:
        messagebox.showinfo("Error","To view detail select one row")

view_button = Button(root, text="View selected candidate",bg="Light Green",font="cooper 15 bold",command=view_selected_row)
view_button.place(x=100,y=710,height=30,width=240)



#====================================Verifying candidate====================================================

def cand_verify():
      selected_item = cand_table.focus()
      if selected_item:
        selected_row = cand_table.item(selected_item, 'values')
        voter_id = selected_row[0]
      else:
        messagebox.showinfo("Error","Please select one row")  

      insert_into_main_database(voter_id)

def insert_into_main_database(voter_id):

      try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ansh@7514",
        database="admin1"
    )
        cursor = connection.cursor()
        select_query="SELECT * FROM candidatever WHERE Voter_id=%s"
        cursor.execute(select_query,(voter_id,))
        candidate_data=cursor.fetchone()

        if candidate_data:
            insert_query="INSERT INTO Candidate_main (Voter_id, Name, Gender, Age, Dob, Address, P_name,S_image,C_image) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s)"
            cursor.execute(insert_query,candidate_data)
        
            delete_query = "DELETE FROM candidatever WHERE Voter_id = %s"
            cursor.execute(delete_query, (voter_id,))
            
        connection.commit()
        connection.close()
       
        
        messagebox.showinfo("Verify","Verified Successfully")
         

      except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")
            
      finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
      



verify_cand=Button(root,text="Verify",bd=2,bg="Light Green",fg="Black",font="cooper 15 bold",command=cand_verify)
verify_cand.place(x=560,y=710,height=30,width=120)


fetch_data_table()

root.mainloop()





