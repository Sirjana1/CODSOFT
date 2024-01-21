import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_var = tk.StringVar(value=12)
        self.generated_password_var = tk.StringVar(value="")

        self.create_widgets()

    def create_widgets(self):
        length_label = ttk.Label(self.root, text="Password Length:")
        length_entry = ttk.Entry(self.root, textvariable=self.length_var, width=5)
        length_label.grid(row=0, column=0, sticky="w")
        length_entry.grid(row=0, column=1, sticky="w")

        generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=1, column=0, columnspan=2, pady=10)

        password_entry = ttk.Entry(self.root, textvariable=self.generated_password_var, state="readonly", width=30)
        password_entry.grid(row=2, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = int(self.length_var.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.generated_password_var.set(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()
