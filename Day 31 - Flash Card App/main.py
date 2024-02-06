from tkinter import *
import pandas
import random
current_card = {}
BACKGROUND_COLOR = "#B1DDC6"

try:
    with open("data/remaining_cards.csv") as data_file:
        words = pandas.read_csv(data_file)
        cards = words.to_dict(orient="records")

except FileNotFoundError:
    with open("data/french_words.csv") as data_file:
        words = pandas.read_csv(data_file)
        cards = words.to_dict(orient="records")


# ---------------------------- FLIP CARD ------------------------------- #


def flip():
    canvas.itemconfig(fc_title, text="English", fill="white")
    canvas.itemconfig(fc_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


# ---------------------------- NEW FLASH CARD ------------------------------- #


def new_flashcard():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(cards)
    canvas.itemconfig(fc_text, text=current_card["French"], fill="black")
    canvas.itemconfig(fc_title, text="French", fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    timer = window.after(3000, flip)

def remove_card():
    global current_card, timer
    cards.remove(current_card)
    new_flashcard()
    data = pandas.DataFrame(cards)
    data.to_csv("data/remaining_cards.csv", index=False)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip)


canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
fc_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
fc_text = canvas.create_text(400, 263, text="text", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=new_flashcard)
wrong.grid(column=1, row=1)


right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, command=remove_card)
right.grid(column=0, row=1)

new_flashcard()
flip()
window.mainloop()
