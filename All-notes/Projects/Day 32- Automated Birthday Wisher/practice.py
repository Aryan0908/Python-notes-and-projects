import json
from tkinter import *
from PIL import ImageTk, Image

BACKGROUND = "white"


def clicked():
    name = name_input.get()
    email = email_input.get()
    day = day_input.get()
    month = month_input.get()
    year = year_input.get()
    print(name)
    new_data = {
        name: {
            "email": email,
            "day": day,
            "month": month,
            "year": year
        }

    }

    try:
        with open("birthday_list.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)

    except FileNotFoundError:
        with open("birthday_list.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        with open("birthday_list.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    name_input.delete(0, END)
    email_input.delete(0, END)
    day_input.delete(0, END)
    month_input.delete(0, END)
    year_input.delete(0, END)

window = Tk()
window.config(bg=BACKGROUND, padx=50, pady=100)
new_canvas = Canvas()
new_canvas.config(height=226, width=417, highlightthickness=0)
new_canvas.grid(column=0, row=0)
birthday_image = ImageTk.PhotoImage(Image.open("happy_birthday.jpg"))
new_canvas.create_image(217, 113, image=birthday_image)

# Name Button
name_input = Entry(width=40)
name_input.insert(0,"Name:")
name_input.grid(column=0, row=1)

# Email Button
email_input = Entry(width=40)
email_input.insert(0,"Email:")
email_input.grid(column=0, row=2)

# Date Button
day_input = Entry(width=10)
day_input.insert(0,"Day")
day_input.grid(column=0, row=3, sticky="W")

# Month Input
month_input = Entry(width=10)
month_input.insert(0, "Month")
month_input.grid(column=0, row=3, )

# Year Input
year_input = Entry(width=10)
year_input.insert(0, "Day")
year_input.grid(column=0, row=3, sticky="E")

# Add Button
add = Button(text="Add", command=clicked)
add.config(width=40)
add.grid(column=0, row=4)


window.mainloop()