# import colorgram

# rgb_colors = []
# colors = colorgram.extract('day_18/image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# 1 -- Create a painting 10 x 10                                                                          
# 2 -- Dot should be 20 at size and 50 space between them                                                           

import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)

turtle.penup()
turtle.hideturtle()

def random_color():
    color = random.choice(color_list)
    return color

def painting_dots():
    for _ in range(10):
        turtle.dot(10, random_color())
        turtle.forward(50)

# painting_dots()
y = 0
x = 0
for _ in range(10):
    painting_dots()
    y+=50
    turtle.goto(x, y)

        
screen = t.Screen()
screen.onclick(screen)

