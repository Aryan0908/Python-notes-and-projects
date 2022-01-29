from tkinter import *

window = Tk()

"""Changing the title of the window"""
window.title("Practice window")

"""Setting a minimum size"""
window.minsize(width=500, height=300)

"""Windows After: After this amount of milliesecond the specified function will be called"""
delay = windows.after(1000, "the function name")

"""Cancelling the windows after"""
window.after_cancel(delay)


# Label
my_label = Label(text="This is a label", font=("Arial", 20, "bold"))

"""Sending the anything to screen"""
my_label.grid(column=0, row=0)

"""Changing arguments"""
my_label["text"] = "New text"
""" OR """
my_label.config(text="New Text")

"""Adding Padding"""
my_label.config(padx=20, pady=20)

# Button

"""Button Command"""


def button_command():
    my_label["text"] = user_input.get()


button = Button(text="Click Me", command=button_command)
button.grid(column=1, row=1)

button_2 = Button(text="Click Me", command=button_command)
button_2.grid(column=2, row=0)

# Entry

user_input = Entry(width=10)
user_input.grid(column=3, row=2)

"""Getting what the user typed"""

print(user_input.get())

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

# Canvas 
canvas = Canvas()

"""Creating things on canvas"""
canvas.create_

"""Changing values of a value in canvas"""
canvas.itemconfig(the_item, "the thing you want to change like text=")

# We can add pading to label, cam=nvas etc. in the grid, pack, pixel

# To keep the window on Screen we use tkinter loop
window.mainloop()
