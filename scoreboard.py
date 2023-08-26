
from turtle import Turtle
class Score(Turtle):
    def __init__(self,player, score, x, y):
        super().__init__()
        self.score = score
        self.player = player
        self.x = x
        self.y = y
        self.penup()
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=self.x, y=self.y)
        self.write(arg=f"P{self.player}: {self.score}", align='center', font=('Arial', 15, 'normal'))

    def if_score(self):
        self.score += 1
        self.update_scoreboard()
