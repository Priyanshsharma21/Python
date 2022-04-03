import time
from turtle import Screen

import pygame.image

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from pygame import mixer

pygame.init()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("pale green")
screen.tracer(0)

player = Player((0, -280))
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, "w")
screen.onkeypress(player.move_backward, "s")

# bgsound
mixer.music.load('roadbg.mp3')
mixer.music.play(-1)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.genrate_car()
    car_manager.move_cars()


    for car in car_manager.all_cars:
        if car.distance(player) < 32:
            car_crash_sound = mixer.Sound('lose.wav')
            car_crash_sound.play()
            game_is_on = False
            scoreboard.gam_over()

    if player.is_finist_line()==True:
        winSound = mixer.Sound('win.wav')
        winSound.play()
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_score()



screen.exitonclick()