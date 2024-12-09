from turtle import Turtle
import random
class food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed(30)
        ran_x=random.randint(-280,280)
        ran_y=random.randint(-280,280)
        self.goto(ran_x,ran_y)

    def refresh(self):
        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 280)
        self.goto(ran_x, ran_y)
