from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.update_level()


    def update_level(self):
        self.goto(x=-250,y=250)
        self.write(f"LEVEL:{self.level}",align="center",font=('Courier',15,'normal'))


    def increase_level(self):
        self.clear()
        self.level+=1
        self.update_level()

        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!",align='center',font=('Courier',45,'bold'))

