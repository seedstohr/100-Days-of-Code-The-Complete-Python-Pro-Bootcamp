from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
game = True

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,  "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")


while game:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
