from turtle import Turtle

class Border_X(Turtle):
    def __init__(self):
        super(Border_X, self).__init__()

        self.shape('square')
        self.shapesize(stretch_wid=35, stretch_len=.5)
        self.color('red')
        self.penup()

    def placement(self, x):
        self.goto(x, 0)

class Border_Y(Turtle):
    def __init__(self):
        super(Border_Y, self).__init__()

        self.shape('square')
        self.shapesize(stretch_wid=.5, stretch_len=35)
        self.color('red')
        self.penup()

    def placement(self, y):
        self.goto(0, y)