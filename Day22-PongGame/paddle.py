from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,left_cor,right_cor):
        super().__init__()
        self.create_paddle(left_cor,right_cor)
    def create_paddle(self,x_cor,y_cor):
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color('white')
        self.goto(x_cor,y_cor)
    def reset(self,left_cor,right_cor):
        self.goto(left_cor,right_cor)
    def go_up(self):
        y_cor=self.ycor()+20
        self.goto(self.xcor(),y_cor)
    def go_down(self):
        y_cor=self.ycor()-20
        self.goto(self.xcor(),y_cor)
