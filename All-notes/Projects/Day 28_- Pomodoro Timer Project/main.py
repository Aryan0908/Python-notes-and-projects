from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    mode.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    work = WORK_MIN
    short_break = SHORT_BREAK_MIN
    long_break = LONG_BREAK_MIN

    global reps
    if reps % 2 == 0:
        mode.config(text="Break", fg=PINK)
        count_down(short_break * 60)

    elif reps == 8:
        mode.config(text="Break", fg=RED)
        count_down(long_break * 60)

    else:
        mode.config(text="Work")
        count_down(work * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = windows.after(1000, count_down, count - 1)

    if count == 0:
        global reps
        reps += 1
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"

        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Pomodoro")
windows.config(padx=100, pady=50, bg=YELLOW)


mode = Label(text="TIMER", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
mode.grid(column=1, row=0)


canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
print(tomato_img)
canvas.create_image(110, 112, image=tomato_img)
timer_text = canvas.create_text(110, 130, text="00:00", font=(FONT_NAME, 28, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", width=5, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=5, highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_mark = Label(bg=YELLOW, fg=GREEN, font=(10))
check_mark.grid(column=1, row=3)


windows.mainloop()