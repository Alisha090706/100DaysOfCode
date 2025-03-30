from turtle import *
# tim=Turtle()
# print(tim)
# tim.shape("turtle")
# tim.color("pink")
# tim.forward(100)
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


# Create turtle screen
screen = Screen()
screen.bgcolor("white")

# Create the turtle
t = Turtle()
t.shape("turtle")
t.color("red")
t.pensize(3)
t.speed(3)

# Function to draw a heart shape
def draw_heart():
    t.begin_fill()
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200) 
    t.forward(133)
    t.end_fill()

# Draw the heart
t.fillcolor("red")
draw_heart()

# Hide turtle and display result
t.hideturtle()
done()
