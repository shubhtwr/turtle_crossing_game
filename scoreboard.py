from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-250, 280)
        self.update()

    def update(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.clear()
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)
