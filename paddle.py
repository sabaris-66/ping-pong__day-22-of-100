from turtle import Turtle
class Paddle:
    def __init__(self):
        self.a = "a"
        self.paddle1 = Turtle('square')
        self.paddle2 = Turtle('square')
        self.position()

    def position(self):
        self.paddle1.penup()
        self.paddle2.penup()
        self.paddle1.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle1.setposition(x=350, y=0)
        self.paddle1.fillcolor('white')
        self.paddle2.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle2.setposition(x=-350, y=0)
        self.paddle2.fillcolor('white')

    def player1_up(self):
        pos = self.paddle1.ycor() + 35
        self.paddle1.goto(350, pos)

    def player1_down(self):
        pos = self.paddle1.ycor() - 35
        self.paddle1.goto(350, pos)

    def player2_up(self):
        pos = self.paddle2.ycor() + 35
        self.paddle2.goto(-350, pos)

    def player2_down(self):
        pos = self.paddle2.ycor() - 35
        self.paddle2.goto(-350, pos)
