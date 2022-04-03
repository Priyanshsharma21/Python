from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):



    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as readFile:
            self.highScore = int(readFile.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highScore}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open('data.txt',mode= 'w') as data:
                data.write(f"{self.highScore}")
        self.score = 0


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
