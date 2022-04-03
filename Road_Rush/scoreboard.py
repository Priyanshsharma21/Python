from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
   def __init__(self):
       super().__init__()
       self.level = 0
       self.penup()
       self.hideturtle()
       self.goto(-280, 250)
       self.update_score()

   def gam_over(self):
       self.goto(-85, 0)
       self.write(f"Game Over", align="left", font=FONT)

   def increase_level(self):
        self.level += 1
        self.update_score()

   def update_score(self):
       self.clear()
       self.write(f"Level- {self.level}", align="left", font=FONT)






