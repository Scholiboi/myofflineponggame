from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

TIME = 1/12


def start_game():
    t = Turtle()
    t.penup()
    t.color("red")
    t.goto(-500, -300)
    t.setheading(90)
    t.pendown()
    for n in range(4):
        if n % 2 == 0:
            t.forward(600)
        else:
            t.forward(1000)
        t.right(90)
    t.hideturtle()


screen = Screen()
screen.setup(width=1100, height=700)
screen.bgcolor("black")
screen.tracer(False)
# screen.setworldcoordinates(-500, -300, 500, 300)

game_is_on = True
start_game()
score = Scoreboard()
paddle = Paddle()
pong = Ball()
n = 0.01
reset = False

screen.listen()
screen.onkey(fun=paddle.move_up_left, key="w")
screen.onkey(fun=paddle.move_down_left, key="s")
screen.onkey(fun=paddle.move_up_right, key="Up")
screen.onkey(fun=paddle.move_down_right, key="Down")

while game_is_on:
    screen.update()
    time.sleep(TIME)
    pong.move()
    for n in range(0,len(paddle.left)):
        if pong.distance(paddle.left[n]) < 20:
            pong.collision_left_paddle()
            TIME = TIME/1.1
        if pong.distance(paddle.right[n]) < 20:
            pong.collision_right_paddle()
            TIME = TIME/1.1
    if pong.xcor() > 490 or pong.xcor() < -490:
        if pong.xcor() > 490:
            score.score1 += 1
        elif pong.xcor() < -490:
            score.score2 += 1
        score.update_score()
        time.sleep(3) 
        pong.refresh()
        paddle.refresh() 
        TIME = 1/12  
    if pong.ycor() > 290 or pong.ycor() < -290:
        pong.collision_walls()

screen.exitonclick()
