import turtle as t
import random

turt = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

turt.speed(0)

def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        turt.circle(100)
        current_heading = turt.heading()
        turt.setheading(current_heading + size_of_gap)
        turt.color(random_color())

draw_spirograph(5)

screen = t.Screen()
screen.onclick(screen)

