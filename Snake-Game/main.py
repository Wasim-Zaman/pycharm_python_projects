import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score_board import  ScoreBoard
from border import Border_X, Border_Y


screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

border_xl = Border_X()
border_xl.placement(-350)
border_xr = Border_X()
border_xr.placement(343)

border_yl = Border_Y()
border_yl.placement(-340)
border_yr = Border_Y()
border_yr.placement(350)



screen.listen()
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')

is_moving = True
while is_moving:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.update()
        score.update()

    if not (-340 <= snake.head.xcor() <= 335):
        # Gameover
        score.gameover()
        is_moving = False
    if not (-340 <= snake.head.ycor() <= 335):
        # Gameover
        score.gameover()
        is_moving = False


screen.exitonclick()