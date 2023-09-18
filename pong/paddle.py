from turtle import Screen, Turtle

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.go_to_start()

    def go_to_start(self):
        self.goto(self.x_cor, self.y_cor)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

