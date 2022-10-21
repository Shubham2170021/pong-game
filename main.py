from turtle import Screen,Turtle
from paddle import Padle
from boll import Boll
from scorecard import ScoreCard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle=Padle((280,0))
l_paddle=Padle((-280,0))
boll_1=Boll()
score=ScoreCard()
screen.listen()

screen.onkey(r_paddle.move_up_r,"Up")
screen.onkey(r_paddle.move_down_r,"Down")
screen.onkey(l_paddle.move_up_l,"u")
screen.onkey(l_paddle.move_down_l,"d")
game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    boll_1.move()
    if boll_1.ycor()>270 or boll_1.ycor()<-270:
        boll_1.bounce_y()
    if boll_1.distance(r_paddle)<50 and boll_1.xcor()>280 or boll_1.distance(l_paddle)<50 and boll_1.xcor()>-280:
        boll_1.bounce_x()
    if boll_1.xcor()<-290:
        score.left_score()
        boll_1.restart()
    if boll_1.xcor()>290:
        score.right_score()
        boll_1.restart()




screen.exitonclick()