from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Monospace", 40, "normal")
COLOR = "white"

class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.color(COLOR)

    def scoreboard(self):
        self.write(f"{self.points}", move=False, align=ALIGNMENT, font=FONT)

    def score_count(self):
        self.points += 1
        self.clear()
        self.scoreboard()
