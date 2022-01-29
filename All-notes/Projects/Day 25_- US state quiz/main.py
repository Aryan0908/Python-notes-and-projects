import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()

score = 0
total_states = []
while score != 50:
    answer_state = screen.textinput(title=f"Guess the state {score}/50", prompt="What's another state name?").title()
    guessed_state = data[data.state == answer_state]
    x_axis = guessed_state.x
    y_axis = guessed_state.y

    if answer_state == "Exit":
        missing_states = [missing for missing in data_list if missing not in total_states]
        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.to_csv("Missing States.csv")
        break

    if not guessed_state.empty and answer_state not in total_states:
        total_states.append(answer_state)
        start_turtle = turtle.Turtle()
        start_turtle.hideturtle()
        start_turtle.penup()
        start_turtle.goto(x=int(x_axis), y=int(y_axis))
        start_turtle.write(arg=answer_state, move=True, align="center", font=("Arial", 10, "normal"))
        score += 1


