from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.refresh()

    def check_distance(self, predator, prey):
        if predator.head.distance(prey) < 15:
            self.refresh()
            predator.extend()

            return True


    def refresh(self):
        self.color(random.choice(COLORS))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


