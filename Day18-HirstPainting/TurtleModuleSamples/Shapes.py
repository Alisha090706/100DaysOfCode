from turtle import Turtle,Screen

import random


screen=Screen()

screen.colormode(255)

def random_color():

    r=random.randint(0,255)

    g=random.randint(0,255)

    b=random.randint(0,255)

    return (r,g,b)



def shapes(turtle,sides):
    turtle.color(random_color())

    for i in range(sides):

        turtle.forward(100)

        turtle.right((360/sides))



timmy_the_turtle=Turtle()

timmy_the_turtle.shape("turtle")

for i in range(3,11):

    shapes(timmy_the_turtle,i)





screen.exitonclick()