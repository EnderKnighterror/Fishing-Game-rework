import csv
import hashlib
import os
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("User management system")
root.geometry("500x400")

ASSETS_FOLDER = "users.csv"


def hash_password(password):
    """Hash the password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()


def save_user(username, hashed_password):
    file_path = os.path.join(ASSETS_FOLDER, 'users.csv')

    with open(file_path, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_password])


def user_exists(username):
    file_path = os.path.join(ASSETS_FOLDER, 'users.csv')

    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    return True
    except FileNotFoundError:
        pass
    return False


def authenticate_user(username, password):
    file_path = os.path.join(ASSETS_FOLDER, 'users.csv')

    hashed_password = hash_password(password)
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == hashed_password:
                return True
    return False


def register():
    username = username_entry.get()
    password = password_entry.get()
    if user_exists(username):
        messagebox.showerror("Error", "User already exists")
        return
    if len(password) < 8 or len(password) > 16:
        messagebox.showerror("Error", "Password length must be between 8 and 16.")
        return
    hashed_password = hash_password(password)
    save_user(username, hashed_password)
    messagebox.showinfo("success", "User created successfully")


def login():
    username = username_entry.get()
    password = password_entry.get()
    if not user_exists(username):
        messagebox.showerror("Error", "User does not exist.")
        return
    if not authenticate_user(username, password):
        messagebox.showerror("Error", "Incorrect password")
        return
    messagebox.showinfo("Success", "Login Successful")


username_label = tk.Label(root, text="Username: ")
username_label.pack(pady=5)

password_label = tk.Label(root, text="Password: ")
password_label.pack(pady=5)

username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_entry = tk.Entry(root)
password_entry.pack(pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

register_button = tk.Button(root, text="Register", command=register)
register_button.pack(pady=5)

login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=5)

root.mainloop()
