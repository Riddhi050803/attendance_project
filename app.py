# app.py

import tkinter as tk
from tkinter import messagebox
from register_user import register_user
from mark_attendance import recognize_user

def start_register():
    roll_no = entry_roll_no.get()
    name = entry_name.get()
    
    if not roll_no or not name:
        messagebox.showwarning("Input Error", "Please enter Roll Number and Name.")
        return
    
    register_user(roll_no, name)
    messagebox.showinfo("Registration", f"User '{name}' registered successfully.")

def start_attendance():
    recognize_user()
    messagebox.showinfo("Attendance", "Attendance process completed.")

# GUI Setup
root = tk.Tk()
root.title("Attendance Management System")

# Roll Number Input
tk.Label(root, text="Roll Number:").grid(row=0, column=0, padx=10, pady=10)
entry_roll_no = tk.Entry(root)
entry_roll_no.grid(row=0, column=1, padx=10, pady=10)

# Name Input
tk.Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=10)

# Buttons
btn_register = tk.Button(root, text="Register User", command=start_register, width=15, bg="blue", fg="white")
btn_register.grid(row=2, column=0, padx=10, pady=10)

btn_attendance = tk.Button(root, text="Mark Attendance", command=start_attendance, width=15, bg="green", fg="white")
btn_attendance.grid(row=2, column=1, padx=10, pady=10)

# Run the GUI
root.mainloop()
