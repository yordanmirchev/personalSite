import random
from tkinter import *
import pandas
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
WORDS_CSV = "./data/french_words.csv"
TO_LEARN_CSV ="./data/to_learn.csv"
# Parameters: mode --> front side is in French/English or random
FRENCH = "French"
ENGLISH = "English"
RANDOM_MODE = "Random"

# Parameters : time_out: how many milliseconds to wait before turn the card
TIME_OUT = 3000

try:
    words_dict = pandas.read_csv(TO_LEARN_CSV).to_dict(orient="records")
    print(f"Reading from {TO_LEARN_CSV}")
except FileNotFoundError:
    words_dict = pandas.read_csv(WORDS_CSV).to_dict(orient="records")
    print(f"Reading from {WORDS_CSV}")


random_word_dict = {}
front_side = ""
back_side = ""
word_front = ""
word_back = ""


# ---------------------- Word gen ---------------------- #

def get_front_back_language():
    mode = RANDOM_MODE
    front_side = ""
    back_side = ""


    if mode == RANDOM_MODE:
        front_side = random.choice([FRENCH, ENGLISH])
    else:
        front_side = mode

    if front_side == ENGLISH:
        back_side = FRENCH
    else:
        back_side = ENGLISH

    return (front_side, back_side)


def get_word():
    global random_word_dict, words_dict, front_side, back_side, word_front, word_back
    random_word_dict = random.choice(words_dict)

    sides = get_front_back_language()
    front_side = sides[0]
    back_side = sides[1]

    word_front = random_word_dict[front_side]
    word_back =  random_word_dict[back_side]

# ---------------------- Flip cards ---------------------- #
def next_card():
    global flip_timer, front_side, word_front
    window.after_cancel(flip_timer)
    get_word()
    canvas.itemconfig(card_title, text=front_side, fill="black")
    canvas.itemconfig(card_word, text=word_front, fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(TIME_OUT, func=flip_card)



def flip_card():
    global word_back
    canvas.itemconfig(card_title, text=back_side, fill="white")
    canvas.itemconfig(card_word, text=word_back, fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def word_learned():
    print(len(words_dict))
    print(f"Remove: {random_word_dict}")
    words_dict.remove(random_word_dict)
    print(len(words_dict))

    pandas.DataFrame.from_dict(words_dict).to_csv(TO_LEARN_CSV, index=False)

    next_card()







# ---------------------- UI setup ---------------------- #

window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

flip_timer = window.after(TIME_OUT, func=flip_card)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Courier", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
button_right = Button(image=right_image, highlightthickness=0, command=word_learned)
button_right.grid(row=1, column=0)

wrong_image = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=1)


next_card()

window.mainloop()
