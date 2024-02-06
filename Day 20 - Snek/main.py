from turtle import Screen
from snek import Snek
from food import Food
from scoreboard import Score
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek!")
screen.tracer(0)

game_is_on = True

snek = Snek()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

while game_is_on:
    snek.move(screen)
    time.sleep(0.08)
    screen.update()
    if snek.head.distance(food) < 15:
        food.change_pos()
        scoreboard.score_up()
        snek.extend()
    if snek.head.xcor() > 280 or snek.head.xcor() < -280 or snek.head.ycor() > 280 or snek.head.ycor() < -280:
        scoreboard.reset()
        snek.reset()
    for segment in snek.snek_segments[3:]:
        if snek.head.distance(segment) < 10:
            scoreboard.reset()
            snek.reset()


screen.exitonclick()
