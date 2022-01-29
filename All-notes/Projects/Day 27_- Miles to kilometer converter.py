from tkinter import *

window = Tk()
window.title("Miles to kilometer converter")
window.config(padx=20, pady=50)

# User Entry
miles = Entry(width=7)
miles.grid(column=1, row=0)

# Label
miles_text = Label(text="Miles", font=("Arial", 10, "normal"))
miles_text.grid(column=2, row=0)
miles_text.config(padx=20)

is_equal_to = Label(text="is equal to", font=("Arial", 10, "normal"))
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=5, pady=10)


def kilo_to_miles():
    return round(float(miles.get()) * 1.609, 2)


kilo_num = Label(text=0, font=("Arial", 10, "normal"))
kilo_num.grid(column=1, row=1)

kilometer = Label(text="Km", font=("Arial", 10, "normal"))
kilometer.grid(column=2, row=1)


def button_command():
    kilo_num.config(text=kilo_to_miles())


calculate = Button(text="Calculate", command=button_command)
calculate.grid(column=1, row=2)







window.mainloop()