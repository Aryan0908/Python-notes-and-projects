import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Choose the color tha you think will win the race!")
all_colors = ["red", "green", "yellow", "blue", "orange", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_game_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(all_colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)




if user_input:
    is_game_on = True

while  is_game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            if turtle.pencolor() == user_input:
                print("Congratulation's, your turtle won")
            else:
                print(f"You lose! {(turtle.pencolor()).title()} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()