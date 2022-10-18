from turtle import Turtle, Screen



kivi = Turtle()

for total_sides in range(3, 11):
    angle = 360 / total_sides
    for _ in range(total_sides):
        kivi.forward(100)
        kivi.right(angle)

screen = Screen()
screen.exitonclick()