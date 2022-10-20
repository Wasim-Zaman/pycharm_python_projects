import colorgram as cg

import rgb_colors
import random
import turtle
import time


# Constants
HEIGHT = 600
WIDTH  = 600

# image path for extracting different colors
color_image = './hirst image.jpg'

# extract different kinds of colors from colorgram module
diff_colors = cg.extract(color_image, 36)

# As we know that colorgram extracts different kinds of colors but we need only rgb for that we have created a module
rgb_cols = rgb_colors.RGBColors().get_rgb_colors(diff_colors)


# setting the colormode to rgb in turtle module
turtle.colormode(255)

# setting up the screen
screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
# setting up turtle
trt = turtle.Turtle()
trt.hideturtle()
trt.penup()
x = -230
y = -200
trt.setpos(x=x, y=y)

number = 0
while number <= (((HEIGHT - y) // 50) * 10):
    # random color
    rand_color = random.choice(rgb_cols)
    trt.dot(20, rand_color)
    trt.forward(50)

    time.sleep(0.01)

    if number % 10 == 0:
        y = y + 50
        trt.setpos(x=x, y=y)

    # increment number for iteration
    number += 1

screen.exitonclick()

