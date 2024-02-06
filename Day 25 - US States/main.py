from turtle import Turtle, Screen
import pandas

image = "blank_states_img.gif"

screen = Screen()
screen.title("U.S. States Game")
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

text = Turtle()
text.hideturtle()
text.penup()





#user_input = screen.textinput("Guess the State", "What's another state's name?")
states = pandas.read_csv("50_states.csv")
list_states = states.state.to_list()
list_xs = states.x.to_list()
list_ys = states.y.to_list()

game_is_on = True
guessed_states = []

while game_is_on:
    num_states = len(guessed_states)
    remaining_states = [state for state in list_states if state not in guessed_states]
    user_input = screen.textinput(f"({num_states}/50)", "What's another state's name?")
    for num in range(0, len(list_states)):
        if list_states[num].lower() == str(user_input).lower() and len(guessed_states) <= 50:
            text.goto(int(list_xs[num]), int(list_ys[num]))
            text.write(list_states[num])
            guessed_states.append(list_states[num])
    if num_states == 50:
        game_is_on = False
        text.goto(0, 0)
        text.write("Congratulations you know all of them!")
    elif str(user_input) == "exit":
        break
    print(remaining_states)


    #text.write(user_input, states[states.state == user_input])

screen.exitonclick()