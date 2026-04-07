from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.resizemode("user")
        self.turtlesize(1,5)
        self.goto(position_x, position_y)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
