from turtle import Turtle

FONT = ("Monospace", 16, "normal")
SCOREBOARD_POSITION = (-240, 270)
GAME_OVER_POSITION = (0, 0)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

    def scoreboard(self):
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.goto(GAME_OVER_POSITION)
        self.write(f"GAME OVER", align="center", font=FONT)
