from turtle import Turtle
import random

COLORS=['red','pink','yellow','green','purple','blue','orange']

class Cars(Turtle):
    def __init__(self):
        self.all_cars=[]
        self.car_speed=5


    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_random=random.randint(-250,250)
            new_car.goto(300,y_random)
            self.all_cars.append(new_car)


    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def level_up(self):
        self.car_speed+=2.5