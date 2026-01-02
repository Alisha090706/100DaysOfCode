from turtle import Turtle

FINISH_LINE=270
STARTING_POSITION=-270
MOVE_DISTANCE=10


class Lil_Turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.go_to_start()


    def move_up(self):
        self.forward(MOVE_DISTANCE)


    def go_to_start(self):
        self.goto(x=0,y=STARTING_POSITION)

        
    def reached_finish_line(self):
        if self.ycor()>FINISH_LINE:
            return True
        return False