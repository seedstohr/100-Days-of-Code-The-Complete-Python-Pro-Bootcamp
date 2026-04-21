import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle ill win the race? Enter a color.")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [125, 75, 25, -25, -75, -125]
all_turtles = []
Race = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    Race = True

while Race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            Race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle won the race.")
            else:
                print(f"You lose! The {winning_color} turtle won the race.")
        distance = random.randint(0,10)
        turtle.forward(distance)


screen.listen()

screen.exitonclick()

