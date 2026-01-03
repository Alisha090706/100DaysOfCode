from tkinter import *
import pandas as pd
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

#---------------------------- FLASH CARD ------------------------------- #
try:
    df=pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df=pd.read_csv("data/german_words.csv")
to_learn=df.to_dict(orient="records")
curr_card={}
def next_card():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    curr_card=random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=curr_card["German"], fill="black")
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,text=curr_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(curr_card)
    next_card()
    data=pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Learn German")

flip_timer=window.after(3000, func=flip_card)

# ---------------------------- CARD SETUP ------------------------------- #
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)

card_front_img=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")

card_background=canvas.create_image(400,263,image=card_front_img)

card_title=canvas.create_text(400,150, text="Title", font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263, text="word", font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

# ---------------------------- BUTTONS SETUP ------------------------------- #
cross=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=cross,highlightthickness=0, command=next_card)
unknown_button.grid(row=1,column=0)

check=PhotoImage(file="images/right.png")
known_button=Button(image=check,highlightthickness=0, command=is_known) 
known_button.grid(row=1,column=1)


next_card()

# ---------------------------- MAIN LOOP ------------------------------- #
window.mainloop()