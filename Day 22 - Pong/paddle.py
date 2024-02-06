from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, startpos):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapetransform(1.0, 0.0, 0.0, 5.0)
        self.setheading(270)
        self.goto(startpos)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
