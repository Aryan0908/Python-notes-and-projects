from turtle import Screen
from snake import Snake, STARTING_POSITONS
from food import Food
from scoreboard import ScoreBoard
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
score = 0

screen.listen()

screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #  Detection with food
    if snake.snake_head.distance(food) < 15:
        snake.grow()
        scoreboard.score_increase()
        food.refresh()

    # Detection with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detection with tail
    for block in snake.all_blocks[1:]:
        if snake.snake_head.distance(block) < 10:

            scoreboard.reset()
            snake.reset()
screen.exitonclick()
