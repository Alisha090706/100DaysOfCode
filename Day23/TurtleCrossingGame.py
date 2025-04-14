from turtle import Screen
import time
from lilTurtle import Lil_Turtle
from Cars import Cars
from scoreboard import Scoreboard


screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.title("TURTLE CROSSING GAME")


turtle=Lil_Turtle()
cars=Cars()
score=Scoreboard()


screen.listen()
screen.onkey(fun=turtle.move_up,key="Up")


is_game_on=True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()

    #detect collision of turtle with cars
    for car in cars.all_cars:
        if car.distance(turtle)<20:
            score.game_over()
            is_game_on=False
    
    #detect if turtle reached the finish line
    if turtle.reached_finish_line():
        turtle.go_to_start()
        cars.level_up()
        score.increase_level()

        
screen.exitonclick()
