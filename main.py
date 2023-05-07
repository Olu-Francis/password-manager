from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    gen_password = ''.join(password_list)
    password.insert(0, gen_password)
    pyperclip.copy(gen_password)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    web_name = website_name.get().title()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Oops", "You've not save any website yet.")
    else:
        if web_name in data:
            usern = data[web_name]['username']
            passwrd = data[web_name]['password']
            messagebox.showinfo(f"{web_name}", f"Username: {usern}\nPassword: {passwrd}")
        else:
            messagebox.showinfo("Oops", f"This website '{web_name}', has not ben save to db.")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_inputs():
    web = website_name.get().title()
    user = username.get()
    passwrd = password.get()
    new_data = {
        web: {
            "username": user,
            "password": passwrd,
    }}

    if len(web) == 0 or len(passwrd) == 0 or len(user) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", 'r') as file:
                # TODO: Check this out
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_name.delete(0, END)
            password.delete(0, END)
            website_name.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_name = Entry(width=38)
website_name.grid(column=1, row=1)
website_name.focus()
username = Entry(width=61)
username.grid(column=1, row=2, columnspan=2)
username.insert(0, "dansmatd123@gmail.com")
password = Entry(width=38)
password.grid(row=3, column=1)

# Buttons
search_btn = Button(text="Search", width=18, command=find_password)
search_btn.grid(row=1, column=2)
generate_btn = Button(text="Generate Password", width=18, command=generate_password)
generate_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=52, command=save_inputs)
add_btn.grid(column=1, row=4, columnspan=2)
window.mainloop()
