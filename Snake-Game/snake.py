from turtle import Turtle

SLICE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20

class Snake:
    def __init__(self):
        self.slices = []
        self.snake_location()
        self.head = self.slices[0]
        self.direction = 'right'


    def snake_location(self):
        for position in SLICE_POSITIONS:
            new_slice = Turtle('square')
            new_slice.color('green')
            new_slice.penup()
            new_slice.goto(position)
            SLICE_POSITIONS.append(position)
            self.slices.append(new_slice)

    def move(self):
        for index in range(len(SLICE_POSITIONS) - 1, 0, -1):
            new_x = self.slices[index - 1].xcor()
            new_y = self.slices[index - 1].ycor()
            self.slices[index].goto(new_x, new_y)
        self.head.forward(MOVE_SPEED)

    def up(self):
        if self.direction == 'left' or self.direction == 'right':
            self.head.setheading(90)
            self.direction = 'up'

    def down(self):
        if self.direction == 'left' or self.direction == 'right':
            self.head.setheading(270)
            self.direction = 'down'

    def left(self):
        if self.direction == 'up' or self.direction == 'down':
            self.head.setheading(180)
            self.direction = 'left'

    def right(self):
        if self.direction == 'up' or self.direction == 'down':
            self.head.setheading(0)
            self.direction = 'right'

