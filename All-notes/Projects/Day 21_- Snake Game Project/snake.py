from turtle import Turtle


STARTING_POSITONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_blocks = []
        self.blocks()
        self.snake_head = self.all_blocks[0]

    def blocks(self):
        for position in STARTING_POSITONS:
            self.add_block(position)

    def add_block(self, position):
        new_block = Turtle(shape="square")
        new_block.color("black")
        new_block.penup()
        new_block.goto(position)
        self.all_blocks.append(new_block)

    def grow(self):
        self.add_block(position=self.all_blocks[-1].position())

    def move(self):
        for blocks in range(len(self.all_blocks) - 1, 0, -1):
            new_x = self.all_blocks[blocks - 1].xcor()
            new_y = self.all_blocks[blocks - 1].ycor()
            self.all_blocks[blocks].goto(new_x, new_y)

        self.snake_head.forward(MOVE_DISTANCE)



    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.all_blocks[0].setheading(RIGHT)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)




