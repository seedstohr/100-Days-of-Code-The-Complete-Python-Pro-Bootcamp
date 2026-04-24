from ball import Ball
from paddle import Paddle
from turtle import Screen
import time
from score import Score

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

game = True

ball = Ball()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

l_scoreboard = Score((-50, 250))
r_scoreboard = Score((50, 250))

screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")

l_scoreboard.scoreboard()
r_scoreboard.scoreboard()

while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()
    if not ball.paddle_bounced:
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.p_bounce()
    if ball.xcor() == 390:
        l_scoreboard.score_count()
        ball.r_move()
    if ball.xcor() == -390:
        r_scoreboard.score_count()
        ball.r_move()

screen.exitonclick()
