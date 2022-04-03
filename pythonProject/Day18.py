# Kachua module (Turtle module)
import random
import turtle
# from turtle import Turtle, Screen
# from turtle import Turtle as t
# import heroes
#
# hero = heroes.gen()
# print(hero)
# poptiya = Turtle()
# c = t()

# chamkadar.circle(180)
#
# poptiya.shape("turtle")
#
# for i in range(1,10):
#     poptiya.color("blue")
#     poptiya.forward(200)
#     poptiya.right(90)
#     poptiya.color("red")
#     poptiya.circle(180)
# -------------------------------------------------------------------------
# color = ["voilet","indigo","blue","orange","red","green","pink"]
#
# def draw_shape(sides):
#     deg = 360 / sides
#     for i in range(sides):
#         poptiya.forward(100)
#         poptiya.right(deg)
#
# def defineSides():
#     for i in range(3,11):
#         poptiya.color(random.choice(color))
#         draw_shape(i)
# defineSides()
# ----------------------------random walk------------------------------------------
#
# color = ["violet","indigo","blue","orange","red","green","pink"]
# direction = [0, 90, 180, 270]
# c.speed("fastest")
# def move_baby(dir):
#     for i in range(400):
#         c.color(random.choice(color))
#         c.pensize(10)
#         c.forward(30)
#         c.setheading(random.choice(dir))
#
# move_baby(direction)
# ------------------------------------------------------------------
# tuples = Ordered items cannot be add or remove from tuple
# it is immutable

# item = (1, 2, 3, 4, 5, 6, 7)


# if we wanna change it we can put it inside a list(tuple) then can change it
# ----------------------------------------rbg colotr------------------
# turtle.colormode(255)
#
# def randomColor():
#     r = random.randint(1,255)
#     b = random.randint(1,255)
#     g = random.randint(1,255)
#     rbg = (r,b,g)
#     return rbg
#
# c.pensize(30)
# for i in range(200):
#     c.color(randomColor())
#     c.forward(50)
#     c.setheading(random.choice(direction))
#

# -------------------Circle baby(spirograph)--------------------------

# def randomColor():
#     r = random.randint(1, 255)
#     b = random.randint(1, 255)
#     g = random.randint(1, 255)
#     rbg = (r, b, g)
#     return rbg
#
# ccolor = randomColor()
#
# def draw_baby(gap_size):
#     for i in range(int(360/gap_size)):
#         c.color("red")
#         c.circle(100)
#         c.setheading(c.heading() + gap_size)
#
# draw_baby(5)
#
# screen = Screen()
# screen.exitonclick()
# ------------------------------------------------------------------
import colorgram
from turtle import Turtle,Screen
import turtle as t
t.colormode(255)

tut = Turtle()
tut.hideturtle()

color = colorgram.extract('img.jfif',30)
rgb_colors = []
for color in color:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_t = (r,g,b)
    rgb_colors.append(rgb_t)

tut.penup()

tut.setheading(225)
tut.forward(300)
tut.setheading(0)
number_of_dots = 100

tut.speed("fastest")




def draw_histogram():
    for i in range(1, number_of_dots+1):
        tut.dot(20, random.choice(rgb_colors))
        tut.forward(50)

        if i%10==0:
            tut.setheading(90)
            tut.forward(50)
            tut.setheading(180)
            tut.forward(500)
            tut.setheading(0)



draw_histogram()

screen = Screen()
screen.exitonclick()