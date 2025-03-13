from random import choice
from tkinter import Button, Canvas, PhotoImage, Tk
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- FLASH CARD ------------------------------- #

flash_card_data_frame = pd.read_csv("data/french_words.csv")
flash_card_dict = flash_card_data_frame.to_dict(orient="records")
current_card = {}
after_id = None


# ---------------------------- CARD FLIP ------------------------------- #
def next_card():
    global current_card
    global after_id
    if after_id:
        window.after_cancel(after_id)
    current_card = choice(flash_card_dict)
    flash_card_dict.remove(current_card)
    card_canvas.itemconfig(card_canvas_image, image=card_front_image)
    card_canvas.itemconfig(card_title, text="French", fill="black")
    card_canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    after_id = window.after(3000, flip_card)


def flip_card():
    card_canvas.itemconfig(card_canvas_image, image=card_back_image)
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_canvas = Canvas(width=800, height=526, highlightthickness=0)
card_canvas_image = card_canvas.create_image(400, 263, image=card_front_image)
card_title = card_canvas.create_text(
    400, 150, text="Title", font=("Ariel", 40, "italic")
)
card_word = card_canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2)
next_card()


wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)


window.mainloop()
