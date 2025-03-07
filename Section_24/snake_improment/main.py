from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

new_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    new_snake.move()
    screen.update()

    # Detect collision with food
    if new_snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        new_snake.extend()

    # Detect collision with wall
    if (
        new_snake.head.xcor() > 280
        or new_snake.head.xcor() < -280
        or new_snake.head.ycor() > 280
        or new_snake.head.ycor() < -280
    ):
        scoreboard.reset()
        new_snake.reset()

    # Detect collision with tail
    for segment in new_snake.segments[1:]:
        if new_snake.head.distance(segment) < 10:
            scoreboard.reset()
            new_snake.reset()


screen.exitonclick()
