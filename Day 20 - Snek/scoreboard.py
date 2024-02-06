from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(-20, 280)
        self.score = 0
        with open("highscore.txt") as highscore:
            self.highscore = int(highscore.read())
        self.write(f"Score:{self.score} Highscore:{self.highscore}", move=False, align="center", font=("Courier", 20, "normal"))

    def score_up(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score} Highscore:{self.highscore}", move=False, align="center", font=("Courier", 20, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as highscore:
                highscore.write(f"{self.highscore}")

        self.score = 0
        self.clear()
        self.write(f"Score:{self.score} Highscore:{self.highscore}", move=False, align="center", font=("Courier", 20, "normal"))
