from tkinter import *
from tkinter import Tk
from tkinter import ttk
from subprocess import call
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import sys

if len(sys.argv) > 1:
    voter_id = sys.argv[1]
else:
    print("Error: Voter ID not provided.")
    sys.exit(1) 

root=Tk()
root.geometry("800x690")

def move_to_main_vote():
    root.destroy()
    call(['python', "eVote.py",voter_id])
    

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

main_frame=Frame(root,bg="Gray")
main_frame.place(y=160,height=470,width=800)

style = ttk.Style()
style.configure("Treeview", font=("Arial", 11)) 
style.configure("Treeview.Heading", font=("Arial 13 bold"))

admin_label=Label(root,text="Below is the Candidate list",font="Rockwell 24  ",bg="White",bd=0)
admin_label.place(x=215,y=115)

table_frame=Frame(main_frame,highlightbackground="Black",highlightthickness=2,bg="white",bd=7,relief=GROOVE)
table_frame.pack(fill=BOTH,expand=True)


y_scroll=Scrollbar(table_frame,orient=VERTICAL)
x_scroll=Scrollbar(table_frame,orient=HORIZONTAL)

cand_table=ttk.Treeview(table_frame,columns=("voter_id","name","gender","age","p_name"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set,height=50)

y_scroll.config(command=cand_table.yview)
x_scroll.config(command=cand_table.xview)
y_scroll.pack(side=RIGHT,fill=Y)
x_scroll.pack(side=BOTTOM,fill=X)

cand_table.heading("voter_id",text="Voter Id")
cand_table.heading("name",text="Name")
cand_table.heading("gender",text="Gender")
cand_table.heading("age",text="Age")
cand_table.heading("p_name",text="Party Name")

cand_table['show']='headings'

cand_table.column("voter_id",width=120)
cand_table.column("name",width=250)
cand_table.column("gender",width=80)
cand_table.column("age",width=50)
cand_table.column("p_name",width=280)

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
        cursor.execute("Select Voter_id,Name,Gender,Age,P_name from Candidate_main")
        data=cursor.fetchall()

        if len(data)!=0:
             cand_table.delete(*cand_table.get_children())
             for row in data:

                  cand_table.insert("",END,values=(row[0], row[1], row[2], row[3], row[4]))
             connection.commit()
        connection.close()     

      except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")
            
      finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

#=========================Selecting row and passing voterid==============================================

def view_selected_row():
    selected_item = cand_table.focus()
    if selected_item:
        selected_row = cand_table.item(selected_item, 'values')
        voter_id = selected_row[0]  # Get the voter ID from the selected row
      
        call(['python', 'eknowcand_data.py', voter_id])
    else:
        messagebox.showinfo("Error","To view detail select one row")

view_button = Button(root, text="View candidate data",bg="Light Green",font="cooper 15 bold",command=view_selected_row)
view_button.place(x=100,y=640,height=30,width=240)

fetch_data_table()
root.mainloop()


"""mycombo=Combobox(frame1,values=["All","Ward1","Ward2","Ward3","Ward4","Ward5"],width=20,font="Arial 14 ")
mycombo.pack(padx=(280,100),pady=(20,10))

mycombo.set("Select Ward")
mycombo.bind('<<ComboboxSelected>>')

backbtn=Button(frame1,text="Search",bg="blue",fg="white",font="BerlinSans 13 bold")
backbtn.place(x=550,y=17)

frame1.pack(padx=(10,500),pady=(10,400))"""



