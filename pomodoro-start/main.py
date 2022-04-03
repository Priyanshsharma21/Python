# ---------------------------- CONSTANTS ------------------------------- #
import math
import pygame
from pygame import mixer

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
music = ["./music/Spring-Flowers.mp3", "./music/on-off.wav", "./music/break-time.wav", "./music/work-time.wav"]
# -------------------------------Music Setup-------------------------------#
pygame.init()

mixer.music.load(music[0])
mixer.music.play(-1)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    start_sound = mixer.Sound(music[1])
    start_sound.play()
    window.after_cancel(timer)
    canvas.itemconfig(timer_count, text="00:00")
    title_label.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_sound = mixer.Sound(music[1])
    start_sound.play()
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps %8 == 0:
        break_music = mixer.Sound(music[2])
        break_music.play()
        countdown(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps %2 == 0:
        break_music = mixer.Sound(music[2])
        break_music.play()
        countdown(break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        work_music = mixer.Sound(music[3])
        work_music.play()
        countdown(work_sec)
        title_label.config(text="Work Time", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = math.floor(count/60)
    seconds = count%60
    if seconds<10: # this show python dynamic type nature
        seconds=f"0{seconds}"

    canvas.itemconfig(timer_count,text=f"{minutes}:{seconds}")
    if count>0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)
bg = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=bg)
timer_count = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# ----------------------Lable-----------------------------#
title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN)
title_label.config(padx=10, pady=10, bg=YELLOW)
title_label.grid(column=1, row=0)
# ---------------------Buttons--------------------------#
start = Button(text="start", highlightthickness=0, command=start_timer)

start.grid(column=0, row=2)
reset = Button(text="reset", highlightthickness=0, command=reset)
reset.grid(column=2, row=2)
# ------------------checkmarks------------#
check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

window.mainloop()
# GUI is event driven, it update itself every second