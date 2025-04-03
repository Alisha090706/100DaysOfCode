from turtle import Turtle, Screen

import random



screen=Screen()



screen.setup(width=500,height=400)


is_race_on=False

user_bet=screen.textinput(title="Make a bet",prompt="Which turtle will win the race? Enter a color: ").lower()



colors=["red","orange","yellow","green","blue","purple"]


y=[-75,-50,-25,0,25,50]

all_turtles=[]


for i in range(0,6):
    new_turtle=Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    random_distance=random.randint(0,10)
    turtle=random.choice(all_turtles)
    turtle.forward(random_distance)

    if turtle.xcor()>=230:

        if turtle.pencolor()==user_bet:

            print(f"You won! The {user_bet} turtle won the race.")

        else:

            print(f"You lose! The {turtle.pencolor()} turtle won the race.")
        

        is_race_on=False


screen.exitonclick()