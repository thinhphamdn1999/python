from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
l_paddle.listen(screen, "w", "s")
r_paddle.listen(screen, "Up", "Down")


ball = Ball()
score = Score()


screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()
    if score.l_score == 5 or score.r_score == 5:
        score.game_over()
        game_is_on = False

screen.exitonclick()
