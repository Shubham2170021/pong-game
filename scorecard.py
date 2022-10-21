from turtle import Turtle

class ScoreCard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score_l=0
        self.score_r=0
        self.color("white")
        self.penup()
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(150,260)
        self.write(self.score_l,False,align="left",font=('Arial', 25, 'normal'))
        self.goto(-150,260)
        self.write(self.score_r,False,align="left",font=('Arial', 25, 'normal'))
        self.hideturtle()
    def left_score(self):
        self.score_l=self.score_l+1
        self.update_score()
        #self.write({self.score_l},False,align="left",font=('Arial', 25, 'normal'))
    def right_score(self):
        self.score_r=self.score_r+1
        self.update_score()
        #self.write({self.score_r},False,align="left",font=('Arial', 25, 'normal'))
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over! Your score is {self.score}",False,align="center",font=('Arial', 15, 'normal'))

