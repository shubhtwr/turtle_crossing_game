from turtle import Turtle

MOVE_DISTANCE = 10
STARTING_POSITION = (0, -280)
FINSH_LINE_Y = (0, 280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.level_up()
        self.setheading(90)

    def go_up(self):
        self.fd(MOVE_DISTANCE)

    def level_up(self):
        self.goto(STARTING_POSITION)