# 1. Event listener -> On ley is a event listener which take key and
# a function that will be triggered
# when a that key is pressed
# 2.Higher order functions-> Function that works with other functions
# 3. Instance -> From a class(bluprint) we can create multiple instance of the object(examples)
# timmu = Turtle()
# tommy = Turtle()
# both of then are seprate instance
# Every istance can have its different state and functionality
# this is why oops is used

# -------------------------------------------------------------------------
from turtle import Turtle, Screen
import random
# -----------------------------------First---------------------------------------------
# ron = Turtle()
# ron.shape("turtle")
#
#
# def move_forward():
#     ron.color("red")
#     ron.forward(100)
#
#
# def move_backward():
#     ron.color("red")
#     ron.backward(100)
#
#
# def anti_clock():
#     ron.color("red")
#     ron.setheading(ron.heading()+10)
#
#
# def clock():
#     ron.color("red")
#     ron.setheading(ron.heading()-10)
#
#
# def clear_Drawing():
#     ron.clear()
#     ron.penup()
#     ron.home()
#     ron.pendown()
#
#
# screen = Screen()
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=anti_clock)
# screen.onkey(key="d", fun=clock)
# screen.onkey(key="c", fun=clear_Drawing)
#
# screen.exitonclick()
# -----------------------------------------Race Game---------------------------------------
isRaceOn = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Enter your bet: ",prompt="Which turtle will win the race, enter color: ")
colors = ["red", "green", "blue", "orange", "purple", "yellow"]
y_positions = [-100,-50,0,50,100]
all_turtle = []
for ti in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[ti])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[ti])
    all_turtle.append(new_turtle)

if user_bet:
    isRaceOn=True

while isRaceOn:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            isRaceOn=False
            winning_color = turtle.pencolor()
            if winning_color==user_bet:
                print(f"Your turtle with {winning_color} won the race")
            else :
                print(f"Your turtle loose, {winning_color} turtle win the race")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
