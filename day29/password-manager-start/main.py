from tkinter import *
from tkinter import messagebox
import pyperclip

import random
SAVE_FILE="password_store.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(0, nr_letters)]
    password_list +=  [random.choice(numbers) for _ in range(0, nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(0, nr_symbols)]

    random.shuffle(password_list)
    password = "".join(password_list)

    pyperclip.copy(password)
    password_entry.insert(0, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    if len(site_entry.get()) > 0 and len(password_entry.get()) > 0:
        input = f"{site_entry.get()} | {user_name_entry.get()} | {password_entry.get()}"

        is_confirmed = messagebox.askokcancel(message=f"Confirm details: {input} ?")

        if is_confirmed:
            with open(SAVE_FILE, mode="a") as data:
                data.write(f"{input}\n")

            site_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(message="Details missing, please check!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, background="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Courier", 15), bg="white")
website_label.grid(row=1, column=0)

site_entry = Entry(width=35)
site_entry.grid(row=1, column=1, columnspan=2)
site_entry.focus()

user_name_label = Label(text="Email/Username:", font=("Courier", 15), bg="white")
user_name_label.grid(row=2, column=0)

user_name_entry = Entry(width=35)
user_name_entry.grid(row=2, column=1, columnspan=2)
user_name_entry.insert(0, "ymm@example.com")

password_label = Label(text="Password:", font=("Courier", 15), bg="white")
password_label.grid(row=3, column=0)

password_entry = Entry(width=23)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate", command=generate_password, font=("Courier", 15),
                         highlightthickness=0)
password_button.grid(row=3, column=2)

add_button = Button(text=" Add ", width=33, command=save_password, font=("Courier", 15),
                    highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
