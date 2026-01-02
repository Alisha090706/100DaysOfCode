from turtle import Turtle,Screen

import random


screen=Screen()

screen.colormode(255)

def random_color():

    r=random.randint(0,255)

    g=random.randint(0,255)

    b=random.randint(0,255)

    return (r,g,b)



def random_walk(turtle):
    turtle.color(random_color())

    angle=random.choice([0,90,180,270])

    turtle.forward(20)

    turtle.setheading(angle)



timmy_the_turtle=Turtle()

timmy_the_turtle.shape("turtle")

timmy_the_turtle.pensize(5)

timmy_the_turtle.speed(10)

for i in range(100):

    random_walk(timmy_the_turtle)






screen.exitonclick()