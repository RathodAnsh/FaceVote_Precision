from tkinter import *
from tkinter import messagebox
from subprocess import call
import mysql.connector

root = Tk()
root.geometry("600x500")

# Function to move to admin dashboard
def move_to_admin_dash():
    root.destroy()
    call(["python", "eElectionmanage.py"])

# Function to calculate font size based on party name length
def calculate_font_size(party_name):
    if len(party_name) <= 15:
        return "Rockwell 14 bold"
    elif len(party_name) <= 20:
        return "Rockwell 12 bold"
    else:
        return "Rockwell 10 bold"

def insert_result_into_database(party_name, total_votes):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ansh@7514",
            database="admin1"
        )
        cursor = connection.cursor()

        # Check if results are already declared
        cursor.execute("SELECT * FROM declare_result")
        existing_result = cursor.fetchone()

        if existing_result:
            messagebox.showinfo("Message", "Results are already declared.")
        else:
            # Insert the details into the declare_result table
            cursor.execute("INSERT INTO declare_result (P_name, Count) VALUES (%s, %s)", (party_name, total_votes))
            connection.commit()
            messagebox.showinfo("Success", "Results declared successfully!")

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error inserting result into database: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Establishing connection to the database
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ansh@7514",
        database="admin1"
    )
    cursor = connection.cursor()

    # Query to get the party name with the maximum count of votes
    cursor.execute("SELECT P_name, COUNT(*) AS total_votes FROM casted_vote GROUP BY P_name ORDER BY total_votes DESC LIMIT 1")
    party_result = cursor.fetchone()
    if party_result:
        party_name_text = party_result[0]
        total_votes_text = party_result[1]
    else:
        party_name_text = "No data available"
        total_votes_text = ""

    # Creating labels and button
    label = Label(root, text="Result Declaration", foreground="Black", font="Rockwell 26 bold underline")
    label.place(x=150, y=10)

    rframe = Frame(root, bg="blue", height=320, width=470)

    label2 = Label(rframe, text="CANDIDATE WON", foreground="White", bg="blue", font="Rockwell 22 bold underline")
    label2.place(x=101, y=10)

    frame = Frame(rframe, bg="White", height=150, width=280)

    party_font_size = calculate_font_size(party_name_text)
    party_name_label = Label(frame, text=f"Party Name: \n{party_name_text}", fg="Black", bg="white", font="Rockwell 14 bold")
    party_name_label.place(x=20, y=20)

    total_votes_label = Label(frame, text=f"Total Votes: {total_votes_text}", fg="Black", bg="white", font="Rockwell 14 bold")
    total_votes_label.place(x=50, y=70)

    frame.place(x=98, y=80)

    # Function call to insert result into database on button click
    declare_btn = Button(rframe, text="Declare", foreground="Black", bg="Pink", font="Rockwell 14 bold", bd=4,
                         command=lambda: insert_result_into_database(party_name_text, total_votes_text))
    declare_btn.place(x=180, y=250, width=120)

    rframe.pack(pady=(100, 0))

    backbtn2 = Button(root, text="Back", bg="Light Gray", fg="Black", font="BerlinSans 15 bold", command=move_to_admin_dash)
    backbtn2.place(x=505, y=430)

    root.mainloop()

except mysql.connector.Error as error:
    messagebox.showerror("Error", f"Error connecting to MySQL: {error}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
