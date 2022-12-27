from turtle import Turtle, Screen

turt = Turtle()
turt.shape("classic")
turt.speed(1)
def draw_shape(num_sides):
    for _ in range(num_sides):
        turt.forward(100)
        turt.right(360 / num_sides)

color_list = ["red", "yellow", "black", "blue","orange", "purple", "green", "grey"]
for shape_side_n in range(3, 11):    
    draw_shape(shape_side_n)
    turt.color(color_list[shape_side_n])
    
screen = Screen()
screen.onclick(screen)

