from turtle import Turtle
import random
init = [-10, 10]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.4, stretch_len=0.4)
        self.x_move = 10
        self.y_move = random.randrange(-10, 10)
        self.move_speed = 0.1

    def move_init(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_pad(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.goto(x=0, y=0)
        self.y_move = random.randrange(-10, 10)
        self.x_move = random.choice(init)
        self.move_speed = 0.1

