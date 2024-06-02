import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

def login():
    # Get user inputs
    username = username_entry.get()
    password = password_entry.get()

    # Validate inputs (you can add more validation as needed)
    if not username or not password:
        messagebox.showerror("Error", "Username and password are required!")
        return

    # Connect to MySQL database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ansh@7514",
            database="sample"
        )
        cursor = connection.cursor()

        # Check if the username and password match
        select_query = "SELECT * FROM data WHERE username = %s AND password = %s"
        user_data = (username, password)
        cursor.execute(select_query, user_data)
        user = cursor.fetchone()
        cursor.fetchall()  # Ensure all results are read

        if user:
            # If user exists, display their details
            display_user_details(user)
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Database Error: {error}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


def display_user_details(user):
    # Create a new window to display user details
    details_window = tk.Toplevel()
    details_window.title("User Details")
    details_window.geometry('400x400')

    # Extract user details
    username, email, photo_path = user[1], user[2], user[3]

    
    if photo_path:
        file_name = "image/" + photo_path.decode("utf-8")  # Assuming file_name contains the name of the image file

        image = Image.open(file_name)
        image = image.resize((100, 100))  # Omit antialiasing parameter
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(details_window, image=photo)
        image_label.image = photo
        image_label.pack(pady=10)


    else:
        no_image_label = tk.Label(details_window, text="No Image Found", font=("Arial", 12))
        no_image_label.pack(pady=10)


    # Display other user details
    username_label = tk.Label(details_window, text=f"Username: {username}", font=("Arial", 12))
    username_label.pack()
    email_label = tk.Label(details_window, text=f"Email: {email}", font=("Arial", 12))
    email_label.pack()

# Create the main window for login
root = tk.Tk()
root.title("Login")
root.geometry('300x200')

# Create labels and entry fields for login
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = ttk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = ttk.Entry(root, show="*")
password_entry.pack()

# Create a button to login
login_button = ttk.Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()
