import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()

screen.onkey(player.up, 'Up')

player.reset_position()

game_is_on = True
while game_is_on:
    time.sleep(car_manager.car_speed)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()


    # detect collision of turtle with a car

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # detect turtle reaching other side

    if player.ycor() == 280:
        print('Successful crossing')
        player.reset_position()
        # recreate cars and speed up the cars
        car_manager.create_cars()
        car_manager.move_cars()
        car_manager.speed_up()




screen.exitonclick()




    # # go to 0,0, if turtle meets car
    # player.reset_position()

