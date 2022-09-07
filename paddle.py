from turtle import Turtle
INIT_X = 370


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=2.7, stretch_len=0.4)
        self.pu()
        self.speed("fastest")
        self.color("white")
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(x=self.xcor(), y=new_y)
