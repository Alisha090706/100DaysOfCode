from turtle import Turtle,Screen
import random


screen=Screen()

screen.colormode(255)

def random_color():

    r=random.randint(0,255)

    g=random.randint(0,255)

    b=random.randint(0,255)

    return (r,g,b)



def spirograph(turtle,size):

    for i in range(int(360/size)):
        turtle.color(random_color())

        turtle.circle(100)

        turtle.setheading(turtle.heading()+size)
        


timmy_the_turtle=Turtle()

timmy_the_turtle.shape("turtle")

timmy_the_turtle.speed(0)


spirograph(timmy_the_turtle,5)



screen.exitonclick()