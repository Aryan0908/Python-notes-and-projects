from tkinter import *
from tkinter import messagebox
import random
import json

LABEL_FONT = "Dongle"

# --------------------------- SEARCHING ----------------------------------------- #


def search():
    with open("data.json", "r") as data_file:
        user_data = json.load(data_file)

    website = website_input.get()
    email = email_input.get()

    password = user_data[website]["password"]
    messagebox.showinfo(title= f"Your {website} info", message=f"Email: {email}\nPassword: {password}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def random_password():
    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    random_letters = [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    random_symbols = [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]

    random_numbers = [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    random.shuffle(password_list)

    generated_password = "".join(password_list)


    password_input.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def all_info():
    website_name = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website_name: {
            "email": email,
            "password": password
        }
    }

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please fill all the fields!")

    else:
        is_ok = messagebox.askokcancel(title="Confirmation",
                                       message=f"This is your credentials for {website_name}:-\nEmail: {email}\n"
                                               f"Password: {password}\nIs it ok to save?")

        if is_ok:

            try:
                with open("data.json", 'r') as data_file:
                    # Reading json file
                    data = json.load(data_file)

                    # Updating json file
                    data.update(new_data)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                with open("data.json", "w") as data_file:
                    # Writing the updated json data
                    json.dump(data, data_file, indent=4)

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(height=300, width=400)
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website:", font=(LABEL_FONT, 10, "normal"))
website_label.grid(row=1, column=0)

website_input = Entry(width=30)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, sticky="W")

# Email
email_label = Label(text="Email/Username:", font=(LABEL_FONT, 10, "normal"))
email_label.grid(row=2, column=0)

email_input = Entry(width=51)
email_input.insert(0, "ryansharma09081990@gmail.com")
email_input.grid(row=2, column=1, columnspan=2, sticky="W")

# Password
password_label = Label(text="Password:", font=(LABEL_FONT, 10, "normal"))
password_label.grid(row=3, column=0)

password_input = Entry(width=30)
password_input.grid(row=3, column=1, sticky="W")

# Search Button
search_button = Button(text="Search", command=search, width=14)
search_button.grid(row=1, column=2, sticky="W")

# Generate Button
generate = Button(text="Generate Password", command=random_password, width=14)
generate.grid(row=3, column=2, sticky="W")

# Add button
add = Button(text="ADD", width=40, command=all_info)
add.grid(row=4, column=1, columnspan=2)



window.mainloop()
