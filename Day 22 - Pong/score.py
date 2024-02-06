from turtle import Turtle

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0
        self.write(f"{self.score}", move=False, align="center", font=("Courier", 50, "normal"))

    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", move=False, align="center", font=("Courier", 50, "normal"))