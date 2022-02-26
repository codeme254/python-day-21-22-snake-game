from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        # super calls the parent's init method inside the child's init method
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=.9, stretch_wid=.9)
        self.color('purple')
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)