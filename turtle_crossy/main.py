from turtle import Screen
import time
from player import Player, FINISH_LINE_Y
from car import Car, MOVE_INCREMENT, START_MOVE_DISTANCE
from score import Score
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_COLOR = "white"
SCREEN_TITLE = "Turtle Crossy"

player = Player()
scoreboard = Score()
cars = []

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)
screen.tracer(0)

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game = True
scoreboard.scoreboard()
car_speed = START_MOVE_DISTANCE

while game:
    screen.update()
    time.sleep(0.1)

    if random.randint(1, 6) == 1:
        cars.append(Car(car_speed))

    for car in cars:
        car.move()
        if player.distance(car) < 20:
            game = False
            scoreboard.game_over()

    if int(player.ycor()) > FINISH_LINE_Y:
        scoreboard.level_up()
        player.reset_position()
        car_speed += MOVE_INCREMENT
        for car in cars:
            car.speed_up()

    cars = [car for car in cars if car.xcor() > -320]

screen.exitonclick()
