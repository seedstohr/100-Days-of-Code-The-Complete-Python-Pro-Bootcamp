from turtle import Turtle

class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def writer_move(self, x, y):
        self.penup()
        self.goto(x, y)

    def write_answer(self, state):
        self.pendown()
        self.write(state, align="center", font=("Arial", 8, "normal"))