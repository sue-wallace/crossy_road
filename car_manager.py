from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10  # to make the car go faster when the game restarts

class CarManager(Turtle):

    def __init__(self):

        self.all_cars = []

    def create_cars(self):
        random_chance = random.randint(1,6)
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

            new_car.car_speed = 0.1

            self.all_cars.append(new_car)

    def move_cars(self):

        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def speed_up(self):

        for car in self.all_cars:
            car.car_speed *= 0.9






        # then move
        # new_x = self.xcor() - STARTING_MOVE_DISTANCE
        # self.goto(new_x, new_y)




