from turtle import Turtle, Screen
from paddle import Paddle
from dot import Ball
import time
from scoreboard import Score
screen = Screen()
screen.title('Pong')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
test = Paddle()
test.position()
ball = Ball()
score1 = Score(1, 0, 100, 200)
score2 = Score(2, 0, -100, 200)
screen.listen()
screen.onkey(fun=test.player1_up, key='Up')
screen.onkey(fun=test.player1_down, key='Down')
screen.onkey(fun=test.player2_up, key='w')
screen.onkey(fun=test.player2_down, key='s ')
game_is_on = True
time_mul = 0.1
while game_is_on:
    time.sleep(time_mul)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    elif (ball.distance(test.paddle1) < 50 and ball.xcor() > 320) or (ball.distance(test.paddle2) < 50 and ball.xcor() < -320):
        ball.pad_bounce()
        time_mul *= 0.9
    elif ball.xcor() > 380:
        score2.if_score()
        ball.x_move *= -1
        ball.home()
        time_mul = 0.1
    elif ball.xcor() < -380:
        score1.if_score()
        ball.x_move *= -1
        ball.home()
        time_mul = 0.1
    ball.ball_move()
    screen.update()

screen.exitonclick()