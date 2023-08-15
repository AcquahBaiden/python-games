import os
# Set environment variable
os.environ['TK_SILENCE_DEPRECATION'] = "1"
import turtle
import random
colors_list = [(199, 12, 31), (195, 67, 21), (213, 13, 9), (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59),
               (35, 33, 154), (240, 246, 251), (14, 205, 222), (18, 27, 60), (244, 42, 159), (71, 8, 51), (55, 24, 11),
               (228, 165, 9), (61, 200, 232), (16, 153, 16), (226, 19, 118), (98, 75, 9), (244, 44, 17), (66, 241, 159),
               (223, 140, 207), (248, 11, 9), (10, 97, 61), (5, 38, 33), (65, 221, 153)]
Tony = turtle.Turtle()

Tony.speed("fastest")
Tony.penup()
Tony.hideturtle()
Tony.setheading(225)
Tony.forward(300)
Tony.heading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    Tony.dot(20, random.choice(colors_list))
    Tony.forward(50)
    if dot_count % 10 == 0:
        Tony.setheading(90)
        Tony.forward(50)
        Tony.setheading(180)
        Tony.forward(500)
        Tony.setheading(0)




screen = turtle.Screen()
screen.exitonclick()
