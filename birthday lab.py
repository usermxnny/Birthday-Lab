import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random

# Create the main window
root = tk.Tk()
root.title("Fun Birthday Program")
root.geometry("400x300")
root.config(bg="lightblue")

def calculate_age():
    # Get user's birthday
    birthdate_str = entry_birthdate.get()
    try:
        # Convert the string to date time object
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

        today = datetime.now()
        age = today.year - birthdate.year
        if(today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        label_result.config(text=f"You are {age} years old!")

        if today.month == birthdate.month and today.day == birthdate.day:
            show_birthday_message(age)
        else:
            messagebox.showinfo("Result", f"You are {age} years old. \nToday is not your birthday.")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter the date in format YYYY-MM-DD.")

def show_birthday_message(age):
    def change_color():
        colors = ["red", "yellow", "green", "blue", "pink", "purple", "orange"]
        label_birthday.config(fg=random.choice(colors))
        root.after(500, change_color)
    label_birthday.config(text=f"Happy Birthday! You are now {age} years old!", font=("Arial", 24, "bold"))
    change_color()

# Birthdate Entry
label_prompt = tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):", bg="lightblue")
label_prompt.pack(pady=10)
entry_birthdate = tk.Entry(root, width=20)
entry_birthdate.pack(pady=5)

button_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="", bg="lightblue", font=("Arial", 12))
label_result.pack(pady=5)

label_birthday = tk.Label(root, text="", bg="lightblue")
label_birthday.pack(pady=30)

# Run the application
root.mainloop()