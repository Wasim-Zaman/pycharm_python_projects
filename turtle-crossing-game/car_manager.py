from turtle import Turtle
import random

COLORS = ['red', 'green', 'blue', 'orange', 'magenta', 'cyan', 'yellow', 'pink', 'brown', 'black', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        new_car = Turtle('square')
        new_car.setheading(180)
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(350, random.randint(-250, 250))
        self.all_cars.append(new_car)

    def create_random_cars(self):
        random_num = random.randint(13,23)
        if random_num == 13:
            self.create_car()

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
