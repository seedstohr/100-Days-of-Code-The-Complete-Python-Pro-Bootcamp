from turtle import Turtle

P_WIDTH = 5
P_HEIGHT = 1
P_COLOR = "white"
P_SHAPE = "square"

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape(P_SHAPE)
        self.penup()
        self.color(P_COLOR)
        self.turtlesize(P_WIDTH, P_HEIGHT)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)