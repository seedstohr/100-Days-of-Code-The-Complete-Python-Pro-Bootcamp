from tkinter import *
import pandas as pd

#constants

BACKGROUND_COLOR = "#B1DDC6"
FLASH_CARD_FRONT = "./images/card_front.png"
FLASH_CARD_BACK = "./images/card_back.png"
CROSS_BUTTON = "./images/wrong.png"
CHECK_MARK_BUTTON ="./images/right.png"
FONT= "Monospace"
LANGUAGE_LABEL_SIZE = 40
WORD_SIZE = 60
LANGUAGE_LABEL_STYLE = "italic"
WORD_STYLE = "bold"
WORD_LIST = "./data/french_words.csv"
WORDS_TO_LEARN = "./data/words_to_learn.csv"
WHITE = "#FFFFFF"
BLACK = "#000000"
WINDOW_TITLE = "Flash Cards"
FlIP_TIMER = 3000

#variable

timer = None

#create window

window = Tk()
window.title(WINDOW_TITLE)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#images

flash_card_image_front = PhotoImage(file=FLASH_CARD_FRONT)
flash_card_image_back = PhotoImage(file=FLASH_CARD_BACK)
cross_button_image = PhotoImage(file=CROSS_BUTTON)
check_mark_button_image = PhotoImage(file=CHECK_MARK_BUTTON)

#generate word pairs

def generate_word_pairs(list_of_words, words_to_learn):

    '''passes in csv to generates a random pair of words from the data frame and assigns variables'''
    global existing_language_language, existing_language_word, new_language_language, new_language_word

    try:

        words_to_learn = pd.read_csv(words_to_learn)
        random_pair = words_to_learn.sample(1)

        new_language_language = words_to_learn.columns[0]
        new_language_word = random_pair[new_language_language].values[0]

        existing_language_language = words_to_learn.columns[1]
        existing_language_word = random_pair[existing_language_language].values[0]
    except FileNotFoundError:

        word_list = pd.read_csv(list_of_words)
        random_pair = word_list.sample(1)

        new_language_language = word_list.columns[0]
        new_language_word = random_pair[new_language_language].values[0]

        existing_language_language = word_list.columns[1]
        existing_language_word = random_pair[existing_language_language].values[0]

def update_index_card():
    '''updates the index card to the new language word than flips to existing language word after x ms'''
    global timer
    if timer:
        window.after_cancel(timer)

    cross_button.config(state="disabled")
    check_mark_button.config(state="disabled")

    flash_card_canvas.itemconfig(flash_card_back_ground_image, image=flash_card_image_front)
    flash_card_canvas.itemconfig(flash_card_language, text=new_language_language, fill=BLACK)
    flash_card_canvas.itemconfig(flash_card_word, text=new_language_word, fill=BLACK)

    flash_card_canvas.after(FlIP_TIMER, flip)

#flip the card

def flip():
    '''flips card to the existing language word changes text color and background image'''
    flash_card_canvas.itemconfig(flash_card_back_ground_image, image=flash_card_image_back)
    flash_card_canvas.itemconfig(flash_card_language, text=existing_language_language, fill=WHITE)
    flash_card_canvas.itemconfig(flash_card_word, text=existing_language_word, fill=WHITE)

    cross_button.config(state="normal")
    check_mark_button.config(state="normal")

#wrong button

def incorrect():
    '''hitting the cross button'''

    generate_word_pairs(WORD_LIST, WORDS_TO_LEARN)
    update_index_card()

#correct button

def correct():
    '''hitting the check mark button and removes make new words to know csv based on clicking the button'''

    global new_language_language, new_language_word, existing_language_language, existing_language_word

    try:
        word_list_df = pd.read_csv(WORDS_TO_LEARN)

        word_list_df = word_list_df[word_list_df[new_language_language] != new_language_word]

        word_list_df.to_csv(WORDS_TO_LEARN, index=False)

    except FileNotFoundError:
        word_list_df = pd.read_csv(WORD_LIST)

        word_list_df = word_list_df[word_list_df[new_language_language] != new_language_word]

        word_list_df.to_csv(WORDS_TO_LEARN, index=False)

    generate_word_pairs(WORD_LIST, WORDS_TO_LEARN)
    update_index_card()

#canvas

flash_card_canvas = Canvas(width= 800, height= 526, highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card_canvas.grid(row=0, column=0, columnspan=2)
flash_card_back_ground_image = flash_card_canvas.create_image(0, 0, image=flash_card_image_front, anchor="nw")
flash_card_language = flash_card_canvas.create_text(400, 150, text="Language", font=(FONT, LANGUAGE_LABEL_SIZE,
                                                                                     LANGUAGE_LABEL_STYLE))
flash_card_word =flash_card_canvas.create_text(400, 263, text="word", font=(FONT, WORD_SIZE, WORD_STYLE))

#buttons

cross_button = Button(image=cross_button_image, command=incorrect, highlightthickness=0, bg=BACKGROUND_COLOR)
cross_button.grid(row=1, column=0)

check_mark_button =Button(image=check_mark_button_image, command=correct, highlightthickness=0, bg=BACKGROUND_COLOR)
check_mark_button.grid(row=1, column=1)

#main loop
generate_word_pairs(WORD_LIST, WORDS_TO_LEARN)
update_index_card()

window.mainloop()
