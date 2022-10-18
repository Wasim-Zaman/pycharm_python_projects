from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('orange')
        self.speed('fastest')
        self.penup()
        self.update()


    def update(self):
        new_x = random.randint(-320, 320)
        new_y = random.randint(-320, 320)
        self.goto(new_x, new_y)