from turtle import Screen
from paddle import Paddle
from Ball import Ball
from scoreboard import ScoreBoard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")

screen.tracer(0)

l_paddle=Paddle(-350,0)
r_paddle=Paddle(350,0)
ball=Ball()
score=ScoreBoard()


screen.listen()
screen.onkey(key="Up",fun=r_paddle.go_up)
screen.onkey(key="Down",fun=r_paddle.go_down)
screen.onkey(key="w",fun=l_paddle.go_up)
screen.onkey(key="s",fun=l_paddle.go_down)
is_game_on=True

while is_game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    
    #detect collision with right paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>=320 or ball.distance(l_paddle)<50 and ball.xcor()<=-320:
        ball.bounce_x()
    #detect ball out of bounds
    if ball.xcor()>380 :
        ball.ball_out_of_bounds()
        l_paddle.reset(-350,0)
        r_paddle.reset(350,0)
        score.l_point()
    if ball.xcor()<-380:
        ball.ball_out_of_bounds()
        l_paddle.reset(-350,0)
        r_paddle.reset(350,0)
        score.r_point()
    
screen.exitonclick()
