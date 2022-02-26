# everything concerning the snake
from turtle import Turtle, Screen

Screen().tracer(0)

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.co_ordinates = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """creates the snake body."""
        for index in range(0, 3):
            snake_body = Turtle("circle")
            # snake_body.shapesize(stretch_len=.2, stretch_wid=.2)
            snake_body.penup()
            snake_body.color("crimson")
            snake_body.goto(self.co_ordinates[index])
            self.segments.append(snake_body)
    
    def increase_snake_size(self):
        new_segment = Turtle('circle')
        # new_segment.hideturtle()
        new_segment.penup()
        new_segment.color('crimson')
        new_segment.goto(self.segments[len(self.segments)-1].xcor(),self.segments[len(self.segments)-1].ycor())
        # new_segment.showturtle()
        self.segments.append(new_segment)
    
    def move(self):
        """Moves the snake forward continuously"""
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)
    
    def up(self):
        """Moves the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Moves the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Moves the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Moves the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    # def pause(self):
    #     self.segments[0].forward(0)
    # def move_on(self):
    #     self.segments[0].forward(20)
