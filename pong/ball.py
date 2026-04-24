from turtle import Turtle

B_WIDTH = 1
B_HEIGHT = 1
B_XCOR = 0
B_YCOR = 0
B_SHAPE = "circle"
B_COLOR = "white"
B_SPEED = "slow"

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.shape(B_SHAPE)
        self.shapesize(B_HEIGHT, B_WIDTH)
        self.color(B_COLOR)
        self.goto(B_XCOR, B_YCOR)
        self.speed(B_SPEED)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.paddle_bounced = False

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)
        if -300 < self.xcor() < 300:
            self.paddle_bounced = False

    def r_move(self):
        self.goto(0, 0)
        self.p_bounce()
        self.move_speed = 0.1

    def bounce(self ):
        self.y_move *= -1

    def p_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        self.paddle_bounced = True






