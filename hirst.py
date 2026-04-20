import turtle
import random

screen = turtle.Screen()
screen.colormode(255)
painter = turtle.Turtle()
painter.speed("fastest")
painter.pensize(20)
painter.hideturtle()

color_list = [(238, 238, 240), (240, 239, 238), (242, 117, 31), (240, 79, 94), (240, 95, 34), (154, 113, 8), (128, 215, 206), (212, 153, 163), (150, 186, 224), (167, 45, 137), (51, 91, 86), (85, 183, 4), (29, 37, 42), (132, 218, 221), (249, 207, 0), (240, 231, 235), (227, 237, 233)]

for row in range(10):
    for column in range(10):
        painter.dot(20)
        painter.color(random.choice(color_list))
        painter.penup()
        painter.forward(50)
    painter.backward(50 * 10)
    painter.left(90)
    painter.forward(50)
    painter.right(90)

screen.exitonclick()
