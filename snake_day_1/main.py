from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
game = True

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,  "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")


while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.scoreboard()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_count()
    if (snake.segments[0].xcor() > 299 or snake.segments[0].xcor() < -299 or
            snake.segments[0].ycor() > 299 or snake.segments[0].ycor() < -299):
        game = False
        scoreboard.gameover()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game = False
            scoreboard.gameover()



screen.exitonclick()