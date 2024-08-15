import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator")

        # Create main frames
        self.input_frame = tk.Frame(self.window)
        self.input_frame.pack()
        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack()
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack()
        self.output_frame = tk.Frame(self.window)
        self.output_frame.pack()

        # Create input field for password length
        self.length_label = tk.Label(self.input_frame, text="Password Length:")
        self.length_label.pack(side=tk.LEFT)
        self.length_entry = tk.Entry(self.input_frame, width=5)
        self.length_entry.pack(side=tk.LEFT)

        # Create checkboxes for password options
        self.uppercase_var = tk.BooleanVar()
        self.uppercase_checkbox = tk.Checkbutton(self.options_frame, text="Include Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_checkbox.pack(side=tk.LEFT)

        self.numbers_var = tk.BooleanVar()
        self.numbers_checkbox = tk.Checkbutton(self.options_frame, text="Include Numbers", variable=self.numbers_var)
        self.numbers_checkbox.pack(side=tk.LEFT)

        self.special_var = tk.BooleanVar()
        self.special_checkbox = tk.Checkbutton(self.options_frame, text="Include Special Characters", variable=self.special_var)
        self.special_checkbox.pack(side=tk.LEFT)

        # Create generate password button
        self.generate_button = tk.Button(self.button_frame, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        # Create output field for generated password
        self.output_label = tk.Label(self.output_frame, text="Generated Password:")
        self.output_label.pack(side=tk.LEFT)
        self.output_entry = tk.Entry(self.output_frame, width=50)
        self.output_entry.pack(side=tk.LEFT)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 8:
                messagebox.showerror("Error", "Password length must be at least 8 characters.")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid password length.")
            return

        characters = string.ascii_lowercase
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.numbers_var.get():
            characters += string.digits
        if self.special_var.get():
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(tk.END, password)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()