FONT = ("Courier", 24, "normal")
INIT_POS = (-200, 250)
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(INIT_POS)
        self.update_level()


    def inc_level(self):
        self.level += 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def gameover(self):
        text = Turtle()
        text.hideturtle()
        text.penup()
        text.goto(0,0)
        text.write('Gameover !', align='center', font=FONT)