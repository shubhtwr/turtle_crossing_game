from turtle import Turtle, Screen
from player import Player
from car_manger import CarManger
from scoreboard import Scoreboard
import time

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car_manger = CarManger()
scoreboard = Scoreboard()

screen.onkey(tim.go_up, "Up")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    car_manger.create_car()
    car_manger.move_cars()
#     detect when turtle collides with the car
    for car in car_manger.all_cars:
        if tim.distance(car) < 20:
            game_on = False
            scoreboard.game_over()

#     detect if the player reaches the other end
    if tim.ycor() > 280:
        tim.level_up()
        car_manger.level_increase()
        scoreboard.score_up()














screen.exitonclick()