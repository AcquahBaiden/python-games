
import random
from turtle import Turtle

colours = ["royal blue", "navy", "lime green", "sea green", "yellow green", "crimson", "dark slate blue"]

tony = Turtle


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tony.forward(300)
        tony.right(angle)


for shape_size in range(3,11):
    tony.color(random.choice(colours))
    draw_shape(shape_size)
