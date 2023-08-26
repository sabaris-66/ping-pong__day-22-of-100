from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10

    def ball_move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce(self):
        self.y_move *= -1

    def pad_bounce(self):
        self.x_move *= -1