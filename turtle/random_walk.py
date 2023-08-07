import random
import turtle

directions = [0, 90, 270, 360]
turtle.colormode(255)
tony = turtle.Turtle()
tony.pensize(10)
tony.speed('fastest')


def random_colour():
    r = random.choice(0, 255)
    g = random.choice(0, 255)
    b = random.choice(0, 255)
    return (r, g, b)


for _ in range(300):
    tony.color(random_colour())
    tony.setheading(random.choice(directions))
    tony.forward(40)


screen = turtle.Screen()
screen.exitonclick()