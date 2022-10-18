from turtle import Turtle
X = 0
Y = 313
FONT = ('Arial', 23, 'normal')
ALIGNMENT = 'center'

class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(X, Y)
        self.write(f'Score: {self.score}', align= ALIGNMENT, font= FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align= ALIGNMENT, font= FONT)
    def gameover(self):
        self.goto(0, 0)
        self.write('😵GAMEOVE😵', align=ALIGNMENT, font=FONT)
