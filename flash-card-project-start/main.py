# import random
# import pandas
# import time
# BACKGROUND_COLOR = "#B1DDC6"
# current_card = {}
# to_know = {}
#
# try :
#
#
# # ----------------------CSV file --------------------------------
#
# data = pandas.read_csv("./data/french_words.csv").to_dict(orient="records")
#
# def card():
#     global current_card, flip_timer
#     window.after_cancel(flip_timer)
#     current_card = random.choice(data)
#     canvas.itemconfig(card_item, text="French", fill="black")
#     canvas.itemconfig(mean_text, text=current_card["French"], fill="black")
#     canvas.itemconfig(canvas_image, image=bg_up_img)
#     flip_timer = window.after(3000, func=swap_card)
#
#
# def swap_card():
#     canvas.itemconfig(canvas_image, image=bg_back_image)
#     canvas.itemconfig(card_item, text="English", fill="white")
#     canvas.itemconfig(mean_text, text=current_card["English"], fill="white")
#
# def is_known():
#     data.remove(current_card)
#     words_to_learn = pandas.DataFrame(data)
#     words_to_learn.to_csv("data/words_to_learn.csv")
#     card()
#
#
#
#
#
#
# # ---------------------UI--------------------------#
# from tkinter import *
#
# window = Tk()
# window.title("Flashy")
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# flip_timer = window.after(3000, func=swap_card)
# bg_back_image = PhotoImage(file="./images/card_back.png")
# bg_up_img = PhotoImage(file="./images/card_front.png")
# canvas = Canvas(width=800, height=526)
# canvas_image = canvas.create_image(400, 263, image=bg_up_img)
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)
# canvas.grid(row=0, column=0, columnspan=2)
# #text canvas
# card_item = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
# mean_text = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
#
# card()
#
# #buttons
#
# correct_img = PhotoImage(file="./images/right.png")
# correct = Button(image=correct_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
# correct.grid(row=1, column=1)
#
# wrong_img = PhotoImage(file="./images/wrong.png")
# wrong = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=card)
# wrong.grid(row=1, column=0)
#
#
# window.mainloop()
#
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()



