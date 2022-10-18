from turtle import Turtle

class Points(Turtle):
    def __init__(self):
        super(Points, self).__init__()

        self.points = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.write(f'Points: {self.points}', False, 'center', font=('Arial', 23, 'normal'))
        self.set_position(0, 0)

    def set_position(self, x, y):
        self.goto(x, y)