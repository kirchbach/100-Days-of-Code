import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


game_is_on = True
scoreboard = Scoreboard()
player = Player()
screen.onkey(player.up, "Up")
car_manager = CarManager()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.car_move()
    for car in car_manager.cars:
        if player.distance(car) < 15:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 280:
        scoreboard.level_up()
        player.goto(0, -280)
        for car in car_manager.cars:
            car_manager.car_faster()

screen.exitonclick()
