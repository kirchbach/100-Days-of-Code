from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-220, 240)
        self.score = 0
        self.write(f"Level {self.score}", move=False, align="center", font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.write(f"Level {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(-10, 0)
        self.write("GAME OVER", move=False, align="center", font=FONT)
