import tkinter as tk
from tkinter import messagebox
import random

def generate_otp():
    otp = random.randint(1000, 9999)
    entry_otp.delete(0, tk.END)
    entry_otp.insert(0, str(otp))

def register():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    phone_number = entry_phone_number.get()
    age = entry_age.get()
    gender = gender_var.get()
    address = text_address.get("1.0", tk.END)
    username = entry_username.get()
    password = entry_password.get()
    otp = entry_otp.get()
    
    #Perform validation
    if not (first_name and last_name and phone_number and age and
            gender and address and username and password and otp):
        messagebox.showerror("Error", "Please fill in all details.")
    elif len(password) < 6:
        messagebox.showerror("Error", "Password should be at least 6 characters long.")
    else:
        messagebox.showinfo("Success", f"Registration successful for {username}!")

#Create main window
root = tk.Tk()
root.title("REGISTRATION FORM")

#Create labels and entry fields
label_first_name = tk.Label(root, text="First Name:", font=("Candara"), fg="black", bg="#f0f0f0")
label_first_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1, padx=10, pady=5)

label_last_name = tk.Label(root, text="Last Name:", font=("Candara"), fg="black", bg="#f0f0f0")
label_last_name.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)

label_phone_number = tk.Label(root, text="Phone Number:", font=("Candara"), fg="black", bg="#f0f0f0")
label_phone_number.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
entry_phone_number = tk.Entry(root)
entry_phone_number.grid(row=2, column=1, padx=10, pady=5)

label_age = tk.Label(root, text="Age:", font=("Candara"), fg="black", bg="#f0f0f0")
label_age.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
entry_age = tk.Entry(root)
entry_age.grid(row=3, column=1, padx=10, pady=5)

label_gender = tk.Label(root, text="Gender:", font=("Candara"), fg="black", bg="#f0f0f0")
label_gender.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
gender_var = tk.StringVar(root)
gender_var.set("--Select--")
gender_menu = tk.OptionMenu(root, gender_var, "Male", "Female", "Other")
gender_menu.grid(row=4, column=1, padx=10, pady=5)

label_address = tk.Label(root, text="Address:", font=("Candara"), fg="black", bg="#f0f0f0")
label_address.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
text_address = tk.Text(root, height=4, width=20)
text_address.grid(row=5, column=1, padx=10, pady=5)

label_username = tk.Label(root, text="Username:", font=("Candara"), fg="black", bg="#f0f0f0")
label_username.grid(row=6, column=0, padx=10, pady=5, sticky=tk.E)
entry_username = tk.Entry(root)
entry_username.grid(row=6, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Password:", font=("Candara"), fg="black", bg="#f0f0f0")
label_password.grid(row=7, column=0, padx=10, pady=5, sticky=tk.E)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=7, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Confirm Password:", font=("Candara"), fg="black", bg="#f0f0f0")
label_password.grid(row=8, column=0, padx=10, pady=5, sticky=tk.E)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=8, column=1, padx=10, pady=5)

label_otp = tk.Label(root, text="OTP:", font=("Candara"), fg="black", bg="#f0f0f0")
label_otp.grid(row=9, column=0, padx=10, pady=5, sticky=tk.E)
entry_otp = tk.Entry(root)
entry_otp.grid(row=9, column=1, padx=10, pady=5)
otp_button = tk.Button(root, text="Generate OTP", command=generate_otp, font=("Candara"), fg="black", bg="#f0f0f0")
otp_button.grid(row=9, column=2, padx=10, pady=5)

# Create register button
register_button = tk.Button(root, text="Register", command=register, font=("Candara"), fg="black", bg="#f0f0f0")
register_button.grid(row=10, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()

