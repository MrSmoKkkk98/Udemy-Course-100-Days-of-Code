from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_names = ["tim", "tom", "den", "dix", "jack", "ronald"]
y_positions = [100, 60, 20, -20, -60, -100]
all_turtles = []

for i in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-235, y=y_positions[i])
    all_turtles.append(turtle)
    
if user_bet:
    is_race_on = True

while is_race_on:
    
    for turt in all_turtles:
        if turt.xcor() > 230:
            is_race_on = False
            winning_color = turt.pencolor()
            if winning_color == user_bet:
                print(f"You're won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = turt.forward(random.randint(0, 10))

screen.exitonclick()