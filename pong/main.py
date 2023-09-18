from turtle import Screen
from paddle import Paddle
LEFT_START = (-350, 0)
RIGHT_START = (350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "a")
screen.onkey(l_paddle.go_down, "z")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
