from hmac import new
import json
from random import choice, randint, shuffle
from tkinter import Button, Canvas, Entry, Label, PhotoImage, Tk, messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def generate_password():
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, "end")
    password_input.insert(0, password)

def save():
    website_value = website_input.get()
    email_value = email_input.get()
    password_value = password_input.get()
    new_data = {website_value: {"email": email_value, "password": password_value}}

    if len(website_value) == 0 or len(password_value) == 0 or len(email_value) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
        return

    try:
        with open("data.json", "r") as data_read_file:
            data = json.load(data_read_file)
            data.update(new_data)
    except FileNotFoundError:
        data = new_data

    with open("data.json", "w") as data_write_file:
        json.dump(data, data_write_file, indent=4)
    website_input.delete(0, "end")
    password_input.delete(0, "end")
    website_input.focus()
    messagebox.showinfo(title="Success", message="Password saved successfully!")

def search():
    website_value = website_input.get()
    try:
        with open("data.json", "r") as data_read_file:
            data = json.load(data_read_file)
            email = data[website_value]["email"]
            password = data[website_value]["password"]
            messagebox.showinfo(
                title=website_value,
                message=f"Email: {email}\nPassword: {password}",
            )
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Error", message=f"No details for {website_value} exists.")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = Entry(width=41)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "abc@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
