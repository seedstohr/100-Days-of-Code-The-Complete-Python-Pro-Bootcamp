import random
import sys

game_difficulty = input("welcome to the guessing game.\n"
      "i am thinking of a number between 1 and 100\n"
      "choose difficulty. type 'easy' or 'hard'\n")

def amount_of_guess():
    if game_difficulty == "easy":
        guesses = 10
    elif game_difficulty == "hard":
        guesses = 5
    else:
        print("your selection is invalid restart the game.")
        sys.exit()
    return guesses

def number_selection():
     chosen_number = random.choice(range(101))
     return chosen_number

chosen_number = number_selection()
guesses_remaining = amount_of_guess()

while guesses_remaining != 0:
    print(f"you have {guesses_remaining} guesses remaining")
    user_guess = int(input("guess a number "))
    if user_guess == chosen_number:
        print("you guessed it")
        sys.exit()
    elif user_guess > chosen_number:
        print("too high")
        guesses_remaining -= 1
    elif user_guess < chosen_number:
        print("too low")
        guesses_remaining -= 1
    if guesses_remaining == 0:
        print("you are out of guesses, restart the game")
        sys.exit()








