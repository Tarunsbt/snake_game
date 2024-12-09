from turtle import Turtle
STARTING=[(0,0),(-20,0),(-40,0)]
distance=20
up=90
down=270
left=180
right=0
class Snake:

    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for i in STARTING:
            self.add_segment(i)


    def add_segment(self,i):
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.goto(i)
        self.segment.append(t)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def reset(self):
        for s in self.segment:
            s.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head=self.segment[0]
    def move(self):
        for a in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[a - 1].xcor()
            new_y = self.segment[a - 1].ycor()
            self.segment[a].goto(new_x, new_y)
        self.segment[0].forward(distance)

    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

