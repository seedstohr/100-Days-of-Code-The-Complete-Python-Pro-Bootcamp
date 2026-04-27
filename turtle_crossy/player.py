from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
PLAYER_SHAPE = "turtle"
PLAYER_COLOR = "green"

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape(PLAYER_SHAPE)
        self.color(PLAYER_COLOR)
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)
