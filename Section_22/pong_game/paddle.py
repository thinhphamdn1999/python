from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def go_up(self):
        if self.ycor() > 240:
            return
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() < -240:
            return
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def listen(self, screen, up_key, down_key):
        screen.listen()
        screen.onkey(self.go_up, up_key)
        screen.onkey(self.go_down, down_key)
