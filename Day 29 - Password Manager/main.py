from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list =[choice(letters) for _ in range(randint(8, 10))]
    symbol_list =[choice(symbols) for _ in range(randint(2, 4))]
    number_list =[choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = mail_entry.get()
    passw = password_entry.get()
    new_data = {
        website: {
                "email": email,
                "password": passw
        }
    }
    if len(website_entry.get()) > 0 and len(mail_entry.get()) > 0 and len(password_entry.get()) > 0:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
    else:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty.")

# ---------------------------FIND PASSWORD----------------------------- #

def find_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            messagebox.showinfo(title=website_entry.get(), message=f"E-Mail: "
                                                                         f"{data[website_entry.get()]['email']}\n"
                                                                         f"Password: "
                                                                         f"{data[website_entry.get()]['password']}\n")
    except KeyError:
        messagebox.showerror(title="no such website", message=f"Sorry, could not find the website "
                                                              f"{website_entry.get()}.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

mail_label = Label(text="E-Mail / Username:")
mail_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

mail_entry = Entry(width=35)
mail_entry.grid(column=1, row=2, columnspan=2)
mail_entry.insert(0, "lylatwars@icloud.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_pw_button = Button(text="Generate Password", command=generate_password)
generate_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)


canvas = Canvas()
image = PhotoImage(file="logo.png")
canvas.config(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)
window.mainloop()