from turtle import Screen, Turtle

import pygame

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
from pygame import mixer

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
# screen.textinput("Welcome to pong:","Enter Player1 name:")
# screen.textinput("Welcome to pong:","Enter Player2 name:")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# bgSound
pygame.init()

mixer.music.load('bgSound.mp3')
mixer.music.play(-1)





game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        bounce_sound = mixer.Sound('ballBounce.wav')
        bounce_sound.play()
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        winSound = mixer.Sound('win.wav')
        winSound.play()
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        winSound = mixer.Sound('win.wav')
        winSound.play()
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()