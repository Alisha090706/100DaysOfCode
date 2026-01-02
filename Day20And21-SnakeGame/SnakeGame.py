from turtle import Screen
import time
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard


screen=Screen()

screen.setup(width=600,height=600)

screen.bgcolor("black")

screen.title("My Snake Game")

screen.tracer(0)

snake=Snake()
food=Food()
score=ScoreBoard()

screen.listen()
screen.onkey(key='Up',fun=snake.up)
screen.onkey(key='Down',fun=snake.down)
screen.onkey(key='Left',fun=snake.left)
screen.onkey(key='Right',fun=snake.right)

screen.update()
game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_is_on=False
        score.game_over()

    #Detect collisin with tail
    for segments in snake.all_segments[1:]:
        if snake.head.distance(segments)<10:
            game_is_on=False
            score.game_over()
           


   



screen.exitonclick()