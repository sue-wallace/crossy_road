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
scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.up, 'Up')

player.reset_position()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # detect collision of turtle with a car

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect turtle reaching other side, start new level

    if player.ycor() > 280:
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()




    # # go to 0,0, if turtle meets car
    # player.reset_position()

