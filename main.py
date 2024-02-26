import pandas
from tkinter import *
from random import choice,randint

WHITE = '#FFFFFF'
RED = '#e7305b'
GREEN = '#9bdeac'
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('transaltion.csv')
    to_learn =original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word, text=french_word, fill=RED)
    flip_timer = window.after(3000, english_card)


def known():
    to_learn.remove(current_card)
    to_learn_data = pandas.DataFrame(to_learn)
    to_learn_data.to_csv('words_to_learn.csv',index=False)
    next_card()


def english_card():
    english_word = current_card['English']
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=english_word, fill=GREEN)


# window
window = Tk()
window.title('Language Learn')
window.config(pady=20, padx=20)
flip_timer = window.after(3000, english_card)

    # canvas
canvas = Canvas(width=400, height=350, highlightthickness=0)
img = PhotoImage(file='card01.png')
canvas.create_image(200, 180, image=img)
card_title = canvas.create_text(200, 130, text='', font=('Ariel', 30, 'italic'), fill=WHITE)
card_word = canvas.create_text(200, 200, text='', font=('Ariel', 40, 'bold'))
canvas.grid(row=0, column=1, columnspan=2)

    # button
right = Button()
right_image = PhotoImage(file='right_small.png')
right.config(image=right_image, highlightthickness=0, command=known)
right.grid(row=1, column=1)

wrong = Button()
wrong_image = PhotoImage(file='wrong_small.png')
wrong.config(image=wrong_image, highlightthickness=0, command=next_card)
wrong.grid(row=1, column=2)

next_card()

window.mainloop()