import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "day_25/us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
correct_guess = []
is_running = True
while is_running:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").capitalize()
    print(answer_state)
    data = pandas.read_csv("day_25/us_states_game/50_states.csv")
    all_states = data["state"].to_list()
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        x = int(state_data["x"])
        print(x)
        y = int(state_data["y"])
        print(y)
        t.setposition([x, y])
        write = t.write(answer_state, align="center")
        score += 1
        correct_guess.append(answer_state)
    print(f"Your score is {score}")
    print(correct_guess)
is_running = False














