from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create()
        self.move_amount_x = 10
        self.move_amount_y = 10

    def create(self):
        self.shape('circle')
        self.color('red')
        self.penup()

    def move(self):
        self.new_x = self.xcor() + self.move_amount_x
        self.new_y = self.ycor() + self.move_amount_y
        self.goto((self.new_x, self.new_y))

    def bounce_x(self):
        self.move_amount_x *= -1

    def bounce_y(self):
        self.move_amount_y *= -1