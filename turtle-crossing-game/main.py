import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

my_turtle = Player()
cars = CarManager()
score_board = Scoreboard()



screen.listen()
screen.onkeypress(my_turtle.move_up, 'Up')

turtle_running = True
while turtle_running:
    time.sleep(0.1)
    screen.update()

    ## creating and moving cas..........
    cars.create_random_cars()
    cars.move()

    # detecting the collisions with each and every car.........
    for car in cars.all_cars:
        if my_turtle.distance(car) <= 20:
            turtle_running = False
            screen.bgcolor('grey')
            score_board.gameover()

    # detect when the turtle reaches other side of the screen....
    if my_turtle.is_reach_to_top():
        my_turtle.reset_position()
        cars.level_up()
        score_board.inc_level()

screen.exitonclick()