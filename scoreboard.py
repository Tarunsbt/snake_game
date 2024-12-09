from turtle import Turtle
with open("data.txt",) as f:
    h=int(f.read())
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=h
        self.color("white")
        self.penup()
        self.goto(0, 266)
        self.pendown()
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score:{self.highscore}", align="center"
                   , font=("Arial", 24, "normal"))

    def increase_score(self):

        self.score+=1

        self.update_score()
    def reset(self):

        if self.score> self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as fi:
                fi.write(f"{self.highscore}")
        self.score=0
        self.update_score()
