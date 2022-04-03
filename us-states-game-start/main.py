import turtle
import pandas
from turtle import Turtle,Screen

screen = Screen()
screen.title("US States")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


data = pandas.read_csv("50_states.csv")
all_States = data.state.to_list()
guess_states = []


while len(guess_states) < len(all_States):
    answer_state = screen.textinput(title=f"Guess all state {len(guess_states)}/{len(all_States)}", prompt="Enter a state:").title()

    if answer_state=="Exit":
        missing_states = [state for state in all_States if state not in guess_states]
        new_state_data = pandas.DataFrame(missing_states)
        new_state_data.to_csv("States_to_learn")
        break

    if answer_state in all_States:
        guess_states.append(answer_state)
        t = Turtle()
        t.penup()
        t.hideturtle()
        state_info = data[data.state == answer_state]
        t.goto(int(state_info.x), int(state_info.y))
        t.write(answer_state) #state_info.state.item()


# Make  a csv













