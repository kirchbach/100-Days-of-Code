from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(3)
        self.shapesize(0.7, 0.7)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        y = self.ycor() + self.y_move
        x = self.xcor() + self.x_move
        self.setposition(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1