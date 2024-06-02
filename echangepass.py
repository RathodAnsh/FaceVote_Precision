from tkinter import *
from tkinter import Tk
from subprocess import call
import sys
import mysql.connector
from tkinter import messagebox

if len(sys.argv) > 1:
    voter_id = sys.argv[1]
else:
    print("Error: Voter ID not provided.")
    sys.exit(1)    

def Update_password():
    # Get old and new passwords from entries
    old_password = old_entry.get()
    new_password = new_entry.get()

    if not old_password or not new_password:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ansh@7514",
            database="voter"
        )

        cursor = connection.cursor()

        # Retrieve the stored password for the given voter ID
        cursor.execute("SELECT Password FROM register_detail WHERE Voterid = %s", (voter_id,))
        row = cursor.fetchone()
        
        if row:  # If voter ID exists in the database
            stored_password = row[0]
            if old_password == stored_password:  # Check if old password matches
                # Update the password in the database
                update_query = "UPDATE register_detail SET Password = %s WHERE Voterid = %s"
                cursor.execute(update_query, (new_password,voter_id))
                connection.commit()
                messagebox.showinfo("Success", "Password updated successfully!")
            else:
                messagebox.showerror("Error", "Incorrect old password!")
        else:
            messagebox.showerror("Error", "Voter ID not found in the database!")

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to update password: {error}")
            
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


root=Tk()
root.geometry("700x400")

def move_to_voter_detail():
    root.destroy()
    call(['python', "eregdetails.py",voter_id])

frame=Frame(root,width=620,height=320,bg="Light Blue")
frame.place(x=40,y=40)

lable=Label(frame,text="Change your Password",foreground="Black",background="Light Blue",font="Rockwell 21 bold",border=0)
lable.place(x=150,y=5)

old_password=Label(frame,text="Old Password  :- ",foreground="Black",background="Light Blue",fg="Black",font="Times 18 ",border=0)
old_password.place(x=120,y=110)
old_entry=Entry(frame,foreground="Black",background="White",font="Times 14 ",border=0,bd=2,width=25)
old_entry.place(x=290,y=110)

new_password=Label(frame,text="New Password :- ",foreground="Black",background="Light Blue",font="Times 18 ",border=0)
new_password.place(x=120,y=170)
new_entry=Entry(frame,foreground="Black",background="White",font="Times 14 ",border=0,bd=2,show="*",width=25)
new_entry.place(x=290,y=170)

confirm= Button(frame,text="Confirm", foreground="White",background="Blue",font="Candara 18 bold",border=0,bd=2,command=Update_password)
confirm.place(x=270,y=210)

skip= Button(frame,text="Skip>>>", foreground="Black",bg="Light blue",font="calibri 18 bold underline",bd=0,cursor="hand2",command=move_to_voter_detail)
skip.place(x=500,y=270)

id_label= Label(frame,text=voter_id, foreground="Black",background="Light Blue",font="Arial 14 bold",border=0,bd=2)
id_label.place(x=250,y=60,width=180)





root.mainloop()

