import turtle
from turtle import Turtle, Screen
from get_screen_coordinates import get_mouse_click_coor


# creating a turtle and screen objects
tur = Turtle()
screen = Screen()

# setting path of the image to the variable
image = "./blank_states_img.gif"

# Adding image to the screen so that we can set the shape of the turtle as the same image
screen.addshape(image)

# setting the shape of the turtle to image
tur.shape(image)

# setting the x, y values of the states using turtle onscreenclick listener
turtle.onscreenclick(get_mouse_click_coor)

# screen.exitonclick()
screen.mainloop()