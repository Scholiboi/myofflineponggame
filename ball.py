from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.setheading(randint(-40, 40))

    def refresh(self):
        self.goto(0, 0)
        self.setheading(randint(-40, 40))
    
    def move(self):
        self.forward(20)

    def collision_walls(self):
        current_heading = self.heading()
        modify_heading = 0
        if self.ycor() > 280:
            if 0 < current_heading < 90:
                modify_heading = current_heading
            elif 90 < current_heading < 180:
                modify_heading = current_heading - 180
        elif self.ycor() < -280:
            if 180 < current_heading < 270:
                modify_heading = current_heading - 180
            elif 270 < current_heading < 360:
                modify_heading = current_heading - 360
        self.setheading(current_heading - 2 * modify_heading)

    def collision_right_paddle(self):
        current_heading = self.heading()
        modify_heading = 0
        if 0 < current_heading < 90:
            modify_heading = current_heading - 90
        elif 270 < current_heading < 360:
            modify_heading = current_heading - 270
        self.setheading(current_heading - 2 * modify_heading)

    def collision_left_paddle(self):
        current_heading = self.heading()
        modify_heading = 0
        if 90 < current_heading < 180:
            modify_heading = current_heading - 90
        elif 180 < current_heading < 270:
            modify_heading = current_heading - 270
        self.setheading(current_heading - 2 * modify_heading)