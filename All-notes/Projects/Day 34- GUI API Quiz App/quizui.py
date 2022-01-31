from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUi:

    def __init__(self, ques: QuizBrain):
        self.quiz = ques
        self.current_score = 0
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score:{self.current_score}", font=("Arial", 11, "normal"), bg=THEME_COLOR,
                            fg="white")
        self.score.grid(column=1, row=0, sticky="E")

        self.canvas = Canvas(height=250, width=300)
        self.ques_text = self.canvas.create_text(150, 125, text="text", font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        tick_image = PhotoImage(file="images/true.png")
        cross_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=tick_image, bg=THEME_COLOR,
                                  command=self.true_input,
                                  highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=cross_image, bg=THEME_COLOR,
                                   command=self.false_input,
                                   highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.display_ques()
        self.window.mainloop()

    def display_ques(self):
        self.canvas.config(bg="White")

        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            current_ques = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=current_ques)

        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.ques_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_input(self):
        user_answer = self.quiz.check_answer(user_answer="True")
        if user_answer is True:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.display_ques )



    def false_input(self):
        user_answer = self.quiz.check_answer(user_answer="False")
        if user_answer is True:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.display_ques)







