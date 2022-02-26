from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Zaph")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
# screen.onkey(key="P", fun=snake.pause)
# screen.onkey(key="c", fun=snake.move_on)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.refresh_scoreboard()
        snake.increase_snake_size()
    if snake.head.xcor()>299 or snake.head.xcor() <= -300 or snake.head.ycor()>299 or snake.head.ycor() <= -300:
        scoreboard.print_game_over()
        game_is_on = False
    
    for segment in snake.segments[1::1]:
        if snake.head.distance(segment) < 10:
            scoreboard.print_game_over()
            game_is_on = False

screen.exitonclick()