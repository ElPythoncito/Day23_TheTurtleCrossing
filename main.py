# -------------------------------------------------- EL PYTHONCITO XD 🐍🐍🐍🐍
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from finish_line import FinishLine
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("ivory")
my_screen.tracer(0)

# ---------------------------------------- My Objects
player = Player()
car_manager = CarManager()
car_manager.hideturtle()
finish_line = FinishLine()
scoreboard = Scoreboard()


finish_line.draw_complete_line()
finish_line.draw_logo()

my_screen.listen()
my_screen.onkeypress(key="Up", fun=player.up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()


    # --------------- Create cars and move
    car_manager.new_car()
    car_manager.move_cars()

    # --------------- Detect crash
    for car in car_manager.my_cars:
        if player.distance(car) < 20:
            scoreboard.draw_game_over()
            game_is_on = False

    # -------------- Detect finishing line
    if player.in_finish_line():
        car_manager.level_up()
        scoreboard.up_level_player()

my_screen.exitonclick()
