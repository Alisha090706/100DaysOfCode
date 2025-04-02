from turtle import Turtle,Screen
import colorgram
import random

screen=Screen()
screen.colormode(255)

rgb=[]
colors=colorgram.extract("Day18/colors.jpg",7)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    rgb.append((r,g,b))


timmy_the_turtle=Turtle()
timmy_the_turtle.hideturtle()
timmy_the_turtle.penup()


timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)

timmy_the_turtle.speed(0)

dot_count=100
for i in range(1,dot_count+1):
    timmy_the_turtle.color(random.choice(rgb))
    timmy_the_turtle.dot(20)
    timmy_the_turtle.forward(50)
    if i%10==0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(50)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(500)
        timmy_the_turtle.setheading(0)



screen.exitonclick()