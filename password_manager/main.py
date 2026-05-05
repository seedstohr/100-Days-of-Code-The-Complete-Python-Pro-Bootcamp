import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

WHITE = "#FFFFFF"
BLACK = "#000000"
USER = "stevenstohr@gmail.com"

#generate password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for c in range(random.randint(8, 10))]

    password_symbols = [random.choice(symbols) for c in range(random.randint(2, 4))]

    password_numbers = [random.choice(numbers) for c in range(random.randint(2, 4))]

    password_list = password_numbers + password_letters +  password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)

#save into data.txt  website | user | pass once added clear boxes

def add_to_list():

    #grab values from ui entry
    website = website_entry.get()
    password = password_entry.get()
    identity = identity_entry.get()

    if website == "" or password == "":
        messagebox.showerror(title="Error", message="Do not leave and fields blank.")

    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                      f"Website: {website} \n"
                                                      f"Email: {identity} \n"
                                                      f"Password: {password} \n"
                                                      f"Is it okay to save?")

        # save data to data.txt
        if is_ok:
            with open ("data.txt", "a") as data_file:
                data_file.write(f"{website} | {identity} | {password}\n")

            #clear entries
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

#setup window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20,)

#setup logo
canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#labels
website_label = tk.Label(text="Website:", font=("Monospace", 12))
website_label.grid(row=1, column=0)

identity_label = tk.Label(text="Email/Username:", font=("Monospace", 12))
identity_label.grid(row=2, column=0)

password_label = tk.Label(text="Password:", font=("Monospace", 12))
password_label.grid(row=3, column=0)

#entries
website_entry = tk.Entry(width=36, highlightthickness=1)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

identity_entry = tk.Entry(width=36, highlightthickness=1)
identity_entry.grid(row=2, column=1, columnspan=2)
identity_entry.insert(0, f"{USER}")

password_entry = tk.Entry(width=20, highlightthickness=1)
password_entry.grid(row=3, column=1)

#buttons
generate_button = tk.Button(text="Generate Password", font=("Monospace", 12), command=generate_password)
generate_button.grid(row=3, column=2)

add_button = tk.Button(width=37,text="Add to List", font=("Monospace", 12), command=add_to_list)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
