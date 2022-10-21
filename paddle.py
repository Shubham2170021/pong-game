from turtle import Turtle
POSTION=[(340,0),(-340,0)]
class Padle(Turtle):
    def __init__(self,POSTION):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.speed("fastest")
        self.penup()
        self.goto(POSTION)

    def move_up_r(self):
        self.new_y=self.ycor()+20
        self.goto(self.xcor(),self.new_y)
    def move_down_r(self):
        self.new_y=self.ycor()-20
        self.goto(self.xcor(),self.new_y)
    def move_up_l(self):
        self.new_y=self.ycor()+20
        self.goto(self.xcor(),self.new_y)
    def move_down_l(self):
        self.new_y=self.ycor()-20
        self.goto(self.xcor(),self.new_y)
