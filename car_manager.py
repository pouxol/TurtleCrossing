from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()

    def create_car(self):
        self.add_car()

    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            t = Turtle()
            t.penup()
            t.color(random.choice(COLORS))
            t.shape("square")
            t.shapesize(stretch_wid=1, stretch_len=2)
            t.setpos(300, random.randint(-250, 250))
            t.setheading(180)
            self.cars.append(t)

    def move_car(self, levelscore=1):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + (levelscore - 1) * MOVE_INCREMENT)
