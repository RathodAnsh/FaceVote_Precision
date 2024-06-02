import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector
import shutil

def register_user():
    # Get user inputs
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    photo_path = photo_path_var.get()  # Get the photo path

    # Validate inputs (you can add more validation as needed)
    if not username or not email or not password or not photo_path:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Connect to MySQL database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="sample"
        )
        cursor = connection.cursor()

        # Insert user data into the database
        insert_query = "INSERT INTO data (username, email, password, photo_path) VALUES (%s, %s, %s, %s)"
        user_data = (username, email, password, photo_path)
        cursor.execute(insert_query, user_data)
        connection.commit()

        messagebox.showinfo("Success", "Registration Successful!")
        
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into MySQL table: {error}")
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


import time

def select_photo():
    try:
        # Allow user to select a photo and save it to the "images" folder
        file_path = filedialog.askopenfilename()
        if file_path:
            # Get the filename from the file path
            file_name = os.path.basename(file_path)
            # Extract the extension
            file_name, file_extension = os.path.splitext(file_name)
            # Get the current timestamp
            timestamp = str(int(time.time()))
            # Generate a unique filename using username and timestamp
            unique_filename = f"{username_entry.get()}_{timestamp}{file_extension}"
            # Save the photo to the "images" folder in the same directory as the script
            image_folder = os.path.join(os.path.dirname(__file__), "images")
            if not os.path.exists(image_folder):
                os.makedirs(image_folder)
            destination_path = os.path.join(image_folder, unique_filename)
            # Copy the photo to the destination path
            shutil.copyfile(file_path, destination_path)
            # Update the photo path variable with the unique filename
            photo_path_var.set(unique_filename)
    except Exception as e:
        print("Error:", e)




# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry('400x400')

# Load and display the image
image = Image.open("voter-removebg-preview.png")  # Provide the path to your image file
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.pack()

# Create labels and entry fields for registration form
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = ttk.Entry(root)
username_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = ttk.Entry(root)
email_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = ttk.Entry(root, show="*")
password_entry.pack()

# Create a button to select photo
select_photo_button = ttk.Button(root, text="Select Photo", command=select_photo)
select_photo_button.pack()

# Create a label to display selected photo path
photo_path_var = tk.StringVar()
photo_path_label = tk.Label(root, textvariable=photo_path_var)
photo_path_label.pack()

# Create a button to register user
register_button = ttk.Button(root, text="Register", command=register_user)
register_button.pack()

root.mainloop()
