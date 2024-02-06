from colorthief import ColorThief
colors = ColorThief("kirby.png")

palette = colors.get_palette(color_count=8)
color_list = []
#
for color in palette:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
     color_list.append(color)

print(color_list)

from turtle import Turtle, Screen
import random

screen = Screen()
screen.screensize(2000, 1000)
screen.colormode(255)


tim = Turtle()
tim.penup()
tim.setx(-200)
tim.sety(-200)
tim.hideturtle()
tim.speed(0)

# color_list = [(101, 190, 171), (100, 164, 209), (207, 137, 182), (213, 230, 240), (56, 179, 154), (49, 124, 170), (187, 222, 211), (25, 26, 26), (217, 163, 85), (239, 212, 97), (189, 89, 132), (124, 73, 114), (160, 209, 185), (89, 126, 186), (237, 160, 182), (242, 206, 217), (51, 154, 194), (46, 134, 112), (64, 30, 45), (136, 83, 61), (90, 49, 60), (143, 207, 229), (175, 185, 215), (185, 134, 58), (224, 175, 169), (213, 73, 61), (29, 32, 50), (98, 48, 45), (45, 57, 96)]



def row():
    for _ in range(0,10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)

def move():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

for _ in range(0,10):
    row()
    move()




screen.exitonclick()