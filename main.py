from turtle import Turtle, Screen
from snake import Snake
from food import food
from scoreboard import scoreboard
import time
s=Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("My Snake Game")
s.tracer(0)

Snake=Snake()
food= food()
scoreboard= scoreboard()
game_on=True

s.listen()
s.onkey(Snake.up,"Up")
s.onkey(Snake.down,"Down")
s.onkey(Snake.left,"Left")
s.onkey(Snake.right,"Right")
while game_on:
 s.update()
 time.sleep(0.1)

 Snake.move()
 if Snake.head.distance(food)< 15:
  food.refresh()
  scoreboard.increase_score()
  Snake.extend()

 #wall
 if Snake.head.xcor()>280 or Snake.head.xcor()<-280 or Snake.head.ycor()>280 or Snake.head.ycor()<-280:

   scoreboard.reset()
   Snake.reset()

 #tail
 for sn in Snake.segment[1:]:
  if Snake.head.distance(sn)<10:
   game_on=False
   scoreboard.game_over()


s.exitonclick()