import os
from datetime import datetime
from playsound import playsound
import pygame
from pygame import mixer

extracted_time = "C:\\Users\\priya\\PycharmProjects\\JARVIS\\data\\data.txt"
ex_time = open(extracted_time, mode='rt')
time = ex_time.read()
Time = str(time)

delete_time = open(extracted_time, mode='r+')
delete_time.truncate(0)
delete_time.close()


def ring(time):
    time_to_set = str(time)
    time_now = time_to_set.replace("edith", "")
    time_now = time_now.replace("set alarm for", "")
    time_now = time_now.replace("set", "")
    time_now = time_now.replace("alarm", "")
    time_now = time_now.replace("for", "")
    time_now = time_now.replace(" and ", ":")

    Alarm_time = str(time_now)
    print(Alarm_time)

    while True:
        curr_time = datetime.now().strftime("%H:%M")

        if curr_time == Alarm_time:
            print("Wake up you need to make money")
            assistant_sound = mixer.Sound('tidin.wav')
            assistant_sound.play()

        elif curr_time > Alarm_time:
            break


ring(Time)
