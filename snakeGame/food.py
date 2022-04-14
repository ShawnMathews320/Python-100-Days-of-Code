from turtle import Turtle

import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5, .5)
        self.color('orange')
        self.speed("fastest")
        self.relocate()

    def relocate(self):  # move the food to a new position after the snake touches it 
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)