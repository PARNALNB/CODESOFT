import tkinter as tk
import random
import string
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        # Get the length of the password from user input
        length = int(entry_length.get())

        if length < 1:
            messagebox.showerror("Error", "Password length must be greater than 0")
            return

        # Define possible characters: uppercase, lowercase, digits, and special characters
        all_characters = string.ascii_letters + string.digits + string.punctuation

        # Generate a random password of the desired length
        password = ''.join(random.choice(all_characters) for _ in range(length))

        # Display the generated password
        label_password.config(text=f"Generated Password: {password}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x200")
window.configure(bg="#f7f7f7")

# Create and place a label and entry widget to specify length
label_length = tk.Label(
    window,
    text="Enter password length:",
    font=("Arial", 12),
    bg="#f7f7f7",
    fg="#333333"
)
label_length.grid(row=0, column=0, padx=10, pady=10)

entry_length = tk.Entry(window, font=("Arial", 12), bd=3, relief="sunken")
entry_length.grid(row=0, column=1, padx=10, pady=10)

# Create a button to trigger password generation
button_generate = tk.Button(
    window,
    text="Generate Password",
    command=generate_password,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12),
    bd=4,
    relief="raised"
)
button_generate.grid(row=1, column=0, columnspan=2, pady=10)

# Create a label to display the generated password
label_password = tk.Label(
    window,
    text="Generated Password: ",
    font=("Arial", 12),
    bg="#ffffff",
    fg="#333333",
    anchor="w",
    relief="sunken",
    padx=5
)
label_password.grid(row=2, column=0, columnspan=2, sticky="we", padx=10, pady=10)

# Make the password display area expandable
window.grid_columnconfigure(1, weight=1)

# Start the GUI event loop
window.mainloop()
