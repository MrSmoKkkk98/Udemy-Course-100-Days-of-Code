from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

# 1. Create a snake body
x_positions = [0, -20, -40]
all_turtles = []

for i in range(3):
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.goto(x=x_positions[i], y=0)
    all_turtles.append(turtle)


























screen.exitonclick()