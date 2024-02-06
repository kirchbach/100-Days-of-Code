import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 7
MOVE_INCREMENT = 0.1


class CarManager:
    def __init__(self):
        self.cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        for num in range(-250, 250, 20):
            ran_num_car = random.randint(0, 120)
            if ran_num_car == 1:
                new_car = Turtle("square")
                new_car.penup()
                new_car.color(random.choice(COLORS))
                new_car.setheading(180)
                new_car.shapetransform(1.0, 0.0, 0.0, 2.0)
                new_car.carspeed = STARTING_MOVE_DISTANCE
                new_car.goto(280, num)
                self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            car.forward(self.carspeed)

    def car_faster(self):
        self.carspeed += MOVE_INCREMENT
