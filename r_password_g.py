import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password():
    password_length = length_var.get()
    password_strength = strength_var.get()

    if password_strength == "Low":
        characters = string.ascii_lowercase
    elif password_strength == "Medium":
        characters = string.ascii_letters
    elif password_strength == "Strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Please choose a strength"

    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated_password)

def copy_to_clipboard():
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

root = tk.Tk()
root.title("Random Password Generator")

length_var = tk.IntVar()
strength_var = tk.StringVar()
strength_var.set("Low")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_combobox = ttk.Combobox(root, textvariable=length_var, values=list(range(6, 21)))
length_combobox.grid(row=0, column=1, padx=10, pady=10)
length_combobox.set(8)

strength_label = tk.Label(root, text="Password Strength:")
strength_label.grid(row=1, column=0, padx=10, pady=10)

strength_combobox = ttk.Combobox(root, textvariable=strength_var, values=["Low", "Medium", "Strong"])
strength_combobox.grid(row=1, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(root, show='*')
password_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
