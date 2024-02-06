from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

with open("data/danish_words.csv") as data:
    words = pandas.read_csv(data)
    to_learn = words.to_dict(orient="record")

# ---------------------------- NEW FC ------------------------------- #


def new_fc():
    global new_card
    new_card = to_learn[random.randint(1, 1000)]
    canvas.itemconfig(fc_word, text=new_card["Deutsch"])
    canvas.itemconfig(fc_lang, image=ger_flag)
    canvas.itemconfig(background, image=card_fr_image)
    window.after(2500, turn)

# ---------------------------- TURN CARD ------------------------------- #


def turn():
    canvas.itemconfig(fc_word, text=new_card["Dänisch"])
    canvas.itemconfig(fc_lang, image=dan_flag)
    canvas.itemconfig(background, image=card_bg_image)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_fr_image = PhotoImage(file="images/card_front.png")
card_bg_image = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 263, image=card_fr_image)
canvas.grid(column=0, row=0, columnspan=2)
ger_flag = PhotoImage(file="images/ger_flag.png")
dan_flag = PhotoImage(file="images/dan_flag.png")
fc_lang = canvas.create_image(395, 180, image=ger_flag)
fc_word = canvas.create_text(395, 350, text="text", font=("Ariel", 60, "bold"))

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=new_fc)
right_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_fc)
wrong_button.grid(column=1, row=1)


window.mainloop()
