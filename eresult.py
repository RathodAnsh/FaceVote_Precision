from tkinter import *
from tkinter import Tk, messagebox
from subprocess import call
import mysql.connector
import sys

if len(sys.argv) > 1:
    voter_id = sys.argv[1]
else:
    print("Error: Voter ID not provided.")
    sys.exit(1) 

root = Tk()
root.geometry("600x500")

def move_to_main_vote():
    root.destroy()
    call(['python', "eVote.py",voter_id])

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ansh@7514",
        database="admin1"
    )
    cursor = connection.cursor()

    # Query to fetch the party name and count from the declare_result table
    cursor.execute("SELECT P_name, Count FROM declare_result")
    result = cursor.fetchone()

    if result:
        party_name_text = result[0]
        count_text = result[1]
    else:
        party_name_text = "No data available"
        count_text = ""

    label = Label(root, text="Result", foreground="Black", font="Rockwell 26 bold underline")
    label.place(x=250, y=10)

    rframe = Frame(root, bg="blue", height=290, width=470)

    label2 = Label(rframe, text="CANDIDATE WON", foreground="White", bg="blue", font="Rockwell 22 bold underline")
    label2.place(x=101, y=10)

    frame = Frame(rframe, bg="White", height=150, width=280)

    party_name_label = Label(frame, text="Party Name:", fg="Black", bg="white", font="Rockwell 14 bold ")
    party_name_label.place(x=57, y=28)

    party_name = Label(frame, text=party_name_text, fg="Black", bg="white", font="Rockwell 14 bold")
    party_name.place(x=57, y=50)

    count_label = Label(frame, text="Count:", fg="Black", bg="white", font="Rockwell 14 bold ")
    count_label.place(x=57, y=80)

    count = Label(frame, text=count_text, fg="Black", bg="white", font="Rockwell 14 bold")
    count.place(x=130, y=80)

    frame.place(x=98, y=80)

    label3 = Label(rframe, text="Congratulations!!", foreground="Pink", bg="blue", font="Rockwell 20 bold")
    label3.place(x=120, y=240)

    rframe.pack(pady=(100, 0))

    backbtn2 = Button(root, text="Back", bg="Light Gray", fg="Black", font="BerlinSans 15 bold", command=move_to_main_vote)
    backbtn2.place(x=505, y=430)

    root.mainloop()

except mysql.connector.Error as error:
    messagebox.showerror("Error", f"Error connecting to MySQL: {error}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
