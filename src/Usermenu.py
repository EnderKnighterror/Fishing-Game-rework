import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("User management system")
root.geometry("300x200")

def register():
    username = username_entry.get()
    if user_exists(username):
        messagebox.showerror("error, User already excists")
        return
    password = generate_password