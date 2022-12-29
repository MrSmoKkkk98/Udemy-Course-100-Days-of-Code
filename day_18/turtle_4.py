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

directions = [0, 90, 180, 270]
turt.shape("classic")
turt.speed(10)
turt.pensize(30)
for _ in range(50):
    turt.forward(30)
    turt.setheading(random.choice(directions))
    turt.color(random_color())



screen = t.Screen()
screen.onclick(screen)

