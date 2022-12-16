import turtle

class Line():
    def __init__(self):
        # setting up the turtle
        self.jimmy = turtle.Turtle()
        self.jimmy.hideturtle()
        self.jimmy.penup()
        self.jimmy.setpos(x=-680, y=0)
        self.jimmy.pendown()
        self.jimmy.pensize(10)
        self.jimmy.speed(speed='slowest')

    def round(self):
    # move the turtle just like a heart beats
        self.jimmy.forward(100)
        self.jimmy.setheading(70)
        self.jimmy.forward(100)
        self.jimmy.setheading(270)
        self.jimmy.forward(200)
        self.jimmy.setheading(70)
        self.jimmy.forward(100)
        self.jimmy.setheading(0)
        self.jimmy.forward(70)
