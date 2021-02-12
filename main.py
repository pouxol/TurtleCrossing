from turtle import Screen
import time
from player import Player, FINISH_LINE_Y
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.title("TurtleCrossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car(levelscore=scoreboard.score)

    # Check if player crossed finishing line
    if player.ycor() >= FINISH_LINE_Y:
        player.start()
        scoreboard.keep_score()

    # Detect collision with car.
    for car in car_manager.cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
