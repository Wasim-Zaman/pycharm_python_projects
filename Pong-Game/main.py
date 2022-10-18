# import libraries......
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Points
import time

# TODO-1 Create a screen....
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)


# TODO-2 Create and move Paddel....
paddle_r = Paddle((350, 0), 'red')
paddle_l = Paddle((-350, 0), 'orange')
ball = Ball()
scorepoints = Points()


screen.listen()
screen.onkey(paddle_r.move_up, 'Up')
screen.onkey(paddle_r.move_down, 'Down')
screen.onkey(paddle_l.move_up, 'w')
screen.onkey(paddle_l.move_down, 's')


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.13)

    ball.move()


    # detect the collision with upper and lower border..................
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(paddle_r) <= 40 and ball.xcor() >= 340:
        ball.bounce_x()
        ball.color('orange')

    # detect collision with right paddle
    if ball.distance(paddle_l) <= 40 and ball.xcor() <= -340:
        ball.bounce_x()
        ball.color('red')


screen.exitonclick()