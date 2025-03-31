import random
import string
import tkinter as tk
from tkinter import messagebox
import time
import itertools

def generate_password():
    length = length_var.get()
    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    
    try:
        length = int(length)
        if length <= 0:
            raise ValueError("Password length must be greater than 0.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive number for the password length.")
        return
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ""
    digits = string.digits if use_numbers else ""
    symbols = string.punctuation if use_symbols else ""
    
    all_characters = lower + upper + digits + symbols
    
    if not all_characters:
        messagebox.showerror("Error", "You must select at least one character set!")
        return
    
    password = "".join(random.choice(all_characters) for _ in range(length))
    animate_hacking_effect(password)

def animate_hacking_effect(password):
    result_label.config(text="Initializing hacking sequence...", fg="red")
    root.update()
    time.sleep(1)
    
    hacking_texts = ["Bypassing firewall...", "Decrypting data...", "Accessing mainframe...", "Generating secure password..."]
    colors = ["#00FF00", "#FFFF00", "#FF4500", "#FF0000"]
    
    for text, color in zip(hacking_texts, colors):
        result_label.config(text=text, fg=color)
        root.configure(bg=color)
        root.update()
        time.sleep(1)
    
    for _ in range(3):
        result_label.config(text="✔ Secure Password Generated!", fg="green")
        root.update()
        time.sleep(0.3)
        result_label.config(text="")
        root.update()
        time.sleep(0.3)
    
    result_label.config(text=f"Generated Password: {password}", fg="green")
    root.configure(bg="#f0f0f0")  # Reset to default background

def animate_button():
    colors = itertools.cycle(["red", "blue", "green", "purple", "orange"])
    for _ in range(10):
        generate_button.config(bg=next(colors))
        root.update()
        time.sleep(0.2)
    generate_button.config(bg="SystemButtonFace")  # Reset color

def start_animation():
    animate_button()
    generate_password()
    
root = tk.Tk()
root.title("Password Generator - Hacking Edition")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#000000")

frame = tk.Frame(root, bg="#000000")
frame.pack(pady=20)

tk.Label(frame, text="Enter Password Length:", bg="#000000", fg="#00FF00").grid(row=0, column=0)
length_var = tk.StringVar()
length_entry = tk.Entry(frame, textvariable=length_var)
length_entry.grid(row=0, column=1)

uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(frame, text="Include Uppercase Letters", variable=uppercase_var, bg="#000000", fg="#00FF00").grid(row=1, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Include Numbers", variable=numbers_var, bg="#000000", fg="#00FF00").grid(row=2, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Include Symbols", variable=symbols_var, bg="#000000", fg="#00FF00").grid(row=3, columnspan=2, sticky="w")

generate_button = tk.Button(root, text="Generate Password", command=start_animation, bg="#00FF00", fg="#000000")
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#000000", fg="#00FF00")
result_label.pack(pady=10)

root.mainloop()