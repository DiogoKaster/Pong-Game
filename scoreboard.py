from turtle import Turtle
FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 220)
        self.increase()

    def r_scorer(self):
        self.r_score += 1
        self.increase()

    def l_scorer(self):
        self.l_score += 1
        self.increase()

    def increase(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 220)
        self.write(self.r_score, align="center", font=FONT)
