from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position, color):
        super(Paddle, self).__init__()

        self.shape('square')
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.points = 0

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)