from turtle import Turtle



score = 0


def high_score_content():
    with open("data.txt", mode="r") as current_high_score:
        return int(current_high_score.read())


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = high_score_content()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=("Arial", 12, "normal"))
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score}" f"    High Score = {self.high_score}", move=False, align="center", font=("Arial", 12, "normal"))

    def score_increase(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as high_score_update:
                high_score_update.write(f"{self.score}")
        self.score = 0
        self.high_score = high_score_content()
        self.update_score()
    # def gave_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(arg="Game Over", move=False, align="center", font=("Arial", 12, "normal"))












