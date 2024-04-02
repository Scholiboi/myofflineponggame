from turtle import Turtle

POSITIONS_X = [-450, 440]
POSITIONS_Y = [-30,-10,10,30]


class Paddle:
    def __init__(self):
        self.left = []
        self.right = []
        self.create_paddle()

    def create_paddle(self):
        for n in range(2):
            for i in range(4):
                t = Turtle()
                t.shape("square")
                t.color("white")
                t.penup()
                t.goto(x=POSITIONS_X[n], y=POSITIONS_Y[i])
                t.setheading(90)
                if n == 0:
                    self.left.append(t)
                elif n == 1:
                    self.right.append(t)

    def move_up_left(self):
        if not self.left[3].ycor() > 230:
            for n in range(0, len(self.left)):
                self.left[n].forward(40)

    def move_down_left(self):
        if not self.left[0].ycor() < -230:
            for n in range(0, len(self.left)):
                self.left[n].backward(40)

    def move_up_right(self):
        if not self.right[3].ycor() > 230:
            for n in range(0, len(self.right)):
                self.right[n].forward(40)

    def move_down_right(self):
        if not self.right[0].ycor() < -230:
            for n in range(0, len(self.right)):
                self.right[n].backward(40)

    def refresh(self):
        for n in range(2):
            for i in range(4):
                if n == 0:
                    self.left[i].goto(x=POSITIONS_X[n], y=POSITIONS_Y[i])
                    self.left[i].setheading(90)
                if n == 1:
                    self.right[i].goto(x=POSITIONS_X[n], y=POSITIONS_Y[i])
                    self.right[i].setheading(90)