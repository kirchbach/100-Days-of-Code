from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score1 = Score((70, 250))
score2 = Score((-70, 250))

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    elif ball.xcor() < -320 and ball.distance(paddle2) < 50 or ball.xcor() > 320 and ball.distance(paddle1) < 50:
        ball.bounce_x()
        ball.move_speed *= 0.9
    elif ball.xcor() < -395:
        score2.score_up()
        ball.move_speed = 0.1
        ball.goto(0, 0)
        ball.move()
    elif ball.xcor() > 395:
        score1.score_up()
        ball.move_speed = 0.1
        ball.goto(0, 0)
        ball.move()





screen.exitonclick()