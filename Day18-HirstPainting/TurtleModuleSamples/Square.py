from turtle import Turtle,Screen


def sqaure(turtle):

    for i in range(4):

        turtle.forward(100)

        turtle.right(90)



timmy_the_turtle=Turtle()

timmy_the_turtle.shape("turtle")

timmy_the_turtle.color("purple")

sqaure(timmy_the_turtle)



screen=Screen()

screen.exitonclick()