from turtle import Turtle
import random


class Food(Turtle):
    """The food class is going to know how to render itself as a small circle
    on the screen. And then every time the snake touches the food, then that
    food is going to move to a new random location."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
