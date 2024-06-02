from tkinter import *
from tkinter import messagebox
from subprocess import call
import mysql.connector

root = Tk()
root.geometry("600x500")

def move_to_admin_dash():
    root.destroy()
    call(["python", "eAdmindash.py"])

def insert_result_into_database(party_name_text, total_votes_text):
    try:
        # Establish connection to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ansh@7514",
            database="admin1"
        )
        cursor = connection.cursor()

        # Check if results are already declared
        cursor.execute("SELECT * FROM declare_result")
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Message", "Results are already declared.")
        else:
            # Check if there are any records in casted_vote table
            cursor.execute("SELECT P_name, COUNT(*) AS total_votes FROM casted_vote GROUP BY P_name ORDER BY total_votes DESC LIMIT 1")
            party_result = cursor.fetchone()

            if party_result:
                party_name_text = party_result[0]
                total_votes_text = party_result[1]

                # Insert data into the declare_result table
                cursor.execute("INSERT INTO declare_result (P_name, Count) VALUES (%s, %s)", (party_name_text, total_votes_text))
                connection.commit()
                messagebox.showinfo("Success", "Results declared successfully!")
            else:
                messagebox.showinfo("Message", "No votes casted yet. Cannot declare results.")

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error connecting to MySQL: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ansh@7514",
        database="admin1"
    )
    cursor = connection.cursor()

    # Fetch data from casted_vote table
    cursor.execute("SELECT P_name, COUNT(*) AS total_votes FROM casted_vote GROUP BY P_name ORDER BY total_votes DESC LIMIT 1")
    party_result = cursor.fetchone()

    if party_result:
        party_name_text = party_result[0]
        total_votes_text = party_result[1]
    else:
        party_name_text = "No data available"
        total_votes_text = ""

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

    count_label = Label(frame, text="Total Votes:", fg="Black", bg="white", font="Rockwell 14 bold ")
    count_label.place(x=57, y=80)

    total_votes = Label(frame, text=total_votes_text, fg="Black", bg="white", font="Rockwell 14 bold")
    total_votes.place(x=170, y=80)

    frame.place(x=98, y=80)

    rframe.pack(pady=(100, 0))

    backbtn2 = Button(root, text="Back", bg="Light Gray", fg="Black", font="BerlinSans 15 bold", command=move_to_admin_dash)
    backbtn2.place(x=505, y=430)

    declare_btn = Button(rframe, text="Declare", foreground="Black", bg="Pink", font="Rockwell 14 bold", bd=4, command=lambda: insert_result_into_database(party_name_text, total_votes_text))
    declare_btn.place(x=170, y=240, width=120)

    root.mainloop()

except mysql.connector.Error as error:
    messagebox.showerror("Error", f"Error connecting to MySQL: {error}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
