from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width=500, height=400)
color_list = ["red", "blue", "yellow", "purple", "green", "orange"]
y_positions = [-125, -75, -25, 25, 75, 125]
all_turtles = []
new_race = True



for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_list[turtle_index])
    new_turtle.goto(-215, y_positions[turtle_index])
    all_turtles.append(new_turtle)

while new_race:
    bet = screen.textinput("Your bet:", "Bet on a color!")

    if bet:
        race_on = True

    while race_on:
        for turtle in all_turtles:
                turtle.forward(randint(0, 10))
                if turtle.xcor() > 230:
                    race_on = False
                    if bet == turtle.pencolor():
                        print("Congratulations!")
                    next_race = screen.textinput("Next race?", f"{turtle.pencolor()} won! Race again?")
                    if next_race == "no":
                        new_race = False
                    screen.clear()
                    turtle.clear()



# heading = 0
# tim.setheading(heading)
#
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def turn_clockwise():
#     tim.right(10)
#
# def turn_counterclockwise():
#     tim.left(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forward,'w')
# screen.onkey(move_backward,'s')
# screen.onkey(turn_clockwise,'a')
# screen.onkey(turn_counterclockwise,'d')
# screen.onkey(clear, 'c')

screen.exitonclick()