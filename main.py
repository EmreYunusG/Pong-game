from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)



r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()

score=Scoreboard()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_on=True

while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    #detecting collision w wall
    if ball.ycor() > 280 or ball.ycor()<-280 :
        ball.bounce_y()
    
    #detecting collision w paddle
    if ball.distance(r_paddle) <50 and ball.xcor() >320 or ball.distance(l_paddle) <50 and ball.xcor() <-320 :
        ball.bounce_x()

    if ball.xcor()>380 :
        ball.reset_position()
        score.l_point()

    if  ball.xcor()<-380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()