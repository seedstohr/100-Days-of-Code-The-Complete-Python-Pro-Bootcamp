from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SHAPE = "square"
CAR_SIZE_WIDTH = 2
CAR_SIZE_HEIGHT = 1

class Car(Turtle):

    def __init__(self, speed=START_MOVE_DISTANCE):
        super().__init__()
        self.hideturtle()
        self.shape(CAR_SHAPE)
        self.penup()
        self.color(random.choice(COLORS))
        ran_y = random.randint(-260, 270)
        self.goto(300, ran_y)
        self.setheading(180)
        self.shapesize(stretch_len=CAR_SIZE_WIDTH, stretch_wid=CAR_SIZE_HEIGHT)
        self.showturtle()
        self.move_distance = speed

    def move(self):
        self.forward(self.move_distance)

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT
