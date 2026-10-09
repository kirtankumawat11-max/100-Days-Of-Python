from tkinter import *
import pandas
from random import randint,choice

BACKGROUND_COLOR= "#2EF5FF"
current_card = {}
to_learn = {}

try :
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else :
    to_learn = data.to_dict(orient="records")

#------------------------SAVE PROGERSS--------------------------#
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

#------------------------CREATE NEW FLASH CARDS-----------------------------#

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_image)
    flip_timer = window.after(3000, func=filp_card)

    # data = pandas.read_csv("data/french_words.csv")
    # random_french_word = choice(data["French"].to_list())
    # canvas.itemconfig(french_word,text=random_french_word)

#--------------------------------------Flip the cards-------------------------------#

def filp_card():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_image)





#------------------------GUI-----------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=filp_card)


# front card
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_image = PhotoImage(file="E:/Pycharm/Project/DAY_31/images/card_front.png")
card_background = canvas.create_image(400,263,image=card_front_image)
card_title = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

# Back card
card_back_image = PhotoImage(file="E:/Pycharm/Project/DAY_31/images/card_back.png")


# Button

# right button
right_image = PhotoImage(file="E:/Pycharm/Project/DAY_31/images/right.png")
known_button = Button(image=right_image,bg=BACKGROUND_COLOR,highlightthickness=0,command= is_known)
known_button.grid(column=1,row=1)

# left button
cross_image = PhotoImage(file="E:/Pycharm/Project/DAY_31/images/wrong.png")
unknown_button = Button(image=cross_image,bg=BACKGROUND_COLOR,highlightthickness=0,command=next_card)
unknown_button.grid(column=0,row=1)



next_card()


window.mainloop()
