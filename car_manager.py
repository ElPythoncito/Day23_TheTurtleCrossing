from turtle import Turtle
import random

COLORS = ["orange red", "light slate gray", "yellow", "lime", "steel blue", "medium purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.my_cars = []
        self.increase_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        random_number = random.randint(1, 7)

        if random_number == 3:
            car = Turtle(shape="square")
            car.color(random.choice(COLORS))
            car.penup()
            car.left(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            x = 310
            y = random.randint(-250, 220)
            car.goto(x, y)
            self.my_cars.append(car)

    def move_cars(self):
        for car in self.my_cars:
            car.forward(self.increase_speed)

    def level_up(self):
        self.increase_speed += MOVE_INCREMENT
