# import colorgram
# colors = colorgram.extract('img.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

import turtle as t
import random

color_list = [(126, 104, 61), (191, 159, 110), (75, 108, 85), (166, 146, 59), (76, 93, 120), (246, 218, 179),
              (25, 48, 67), (190, 140, 166), (235, 207, 109), (142, 68, 99), (149, 152, 182), (146, 23, 63),
              (23, 58, 49), (190, 87, 128), (239, 201, 218), (62, 49, 33), (134, 163, 134), (180, 104, 90),
              (38, 50, 114), (72, 31, 53), (109, 115, 167), (38, 79, 60), (228, 168, 195), (105, 151, 90), (83, 75, 30),
              (206, 203, 230), (182, 178, 221), (234, 173, 160), (139, 36, 25), (43, 71, 78)]


tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.penup()
tim.setheading(225)

for _ in range(0, 6):
    tim.forward(50)

tim.setheading(0)
tim.hideturtle()
def draw_line():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.back(500)
    tim.setheading(90)
    tim.forward(50)
    tim.right(90)

for _ in range(9):
    draw_line()


draw_line()


screen = t.Screen()
screen.exitonclick()
