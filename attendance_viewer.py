# attendance_viewer.py

import tkinter as tk
from tkinter import scrolledtext

def load_attendance():
    """Load the attendance file and display it in the text area."""
    try:
        with open("attendance.txt", "r") as file:
            data = file.read()
            text_area.config(state='normal')  # Enable editing to insert text
            text_area.delete(1.0, tk.END)  # Clear existing text
            text_area.insert(tk.END, data)  # Insert attendance data
            text_area.config(state='disabled')  # Disable editing after insertion
    except FileNotFoundError:
        text_area.config(state='normal')
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "No attendance record found.")
        text_area.config(state='disabled')

# Setting up the GUI window
root = tk.Tk()
root.title("Attendance Records Viewer")
root.geometry("400x300")

# Label
label = tk.Label(root, text="Attendance Records", font=("Helvetica", 14))
label.pack(pady=10)

# Scrolled text area to display attendance
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, font=("Helvetica", 10))
text_area.pack(pady=10)
text_area.config(state='disabled')  # Disable editing

# Button to refresh and load the attendance records
refresh_button = tk.Button(root, text="Refresh Attendance", command=load_attendance)
refresh_button.pack(pady=5)

# Load attendance records when the app starts
load_attendance()

# Run the Tkinter event loop
root.mainloop()
