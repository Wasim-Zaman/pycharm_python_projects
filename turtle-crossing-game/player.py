from turtle import Turtle
import random

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
TURTLE_COlORS = ['red', 'green', 'blue', 'orange', 'magenta', 'cyan', 'yellow', 'pink', 'brown', 'black', 'purple']

class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape('turtle')
        self.color(random.choice(TURTLE_COlORS))
        self.penup()
        self.reset_position()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def is_reach_to_top(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False