from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
delay = None
# ------------------------ Reading and Printing data -------------------------- #

try:
    words_left_to_learn = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

    new_data = pandas.DataFrame(data)
    new_data.to_csv("words_left_to_learn.csv", index=False)


data = pandas.read_csv("words_left_to_learn.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)

random_word = {}


def random_card():
    global random_word, timer
    window.after_cancel(timer)
    random_word = random.choice(to_learn)
    french_word = random_word["French"]

    # French Word
    canvas.itemconfig(create_image, image=front_image)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{french_word}", fill="black")
    print(random_word)
    timer = window.after(3000, english)


def english():
    # English Word
    global random_word
    english_word = random_word["English"]
    canvas.itemconfig(create_image, image=back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{english_word}", fill="white")

def is_known():
    global to_learn, random_word
    to_learn.remove(random_word)
    updated_data = pandas.DataFrame(to_learn)
    updated_data.to_csv("words_left_to_learn.csv", index=False)
    random_card()

# ------------------------ UI -------------------------- #

# Main Windows
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
timer = window.after(3000, english)

# Canvas
canvas = Canvas()
canvas.config(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
tick_image = PhotoImage(file="images/right.png")
cross_image = PhotoImage(file="images/wrong.png")

# Cards
create_image = canvas.create_image(400, 263, image=front_image)

# Text
language_text = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT, 60, "bold"))

# Buttons
cross_button = Button(image=cross_image, bg=BACKGROUND_COLOR, command=random_card, highlightthickness=0)
cross_button.grid(column=0, row=1)

tick_button = Button(image=tick_image, command=is_known, highlightthickness=0)
tick_button.grid(column=1, row=1)

random_card()

window.mainloop()
