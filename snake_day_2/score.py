from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Monospace", 20, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0

    def scoreboard(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.points}", move=False, align=ALIGNMENT, font=FONT)

    def score_count(self):
        self.points += 1
        self.clear()
        self.scoreboard()

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", False, ALIGNMENT, FONT)