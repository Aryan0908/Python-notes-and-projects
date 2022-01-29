from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.listen()


def forward():
    timmy.forward(10)


def backward():
    timmy.back(10)


def clockwise():
    timmy.right(5)


def anti_clockwise():
    timmy.left(5)


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()

screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="a", fun=anti_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
