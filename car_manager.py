from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):

        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 5)

        # only create a car from a 1 in 5 chance (so cars aren't created too often)

        if random_chance == 1:

            new_car = Turtle('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.x_cor = 280
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            new_car.left(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)

            self.all_cars.append(new_car)

    def move_cars(self):

        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):

        self.car_speed += MOVE_INCREMENT





