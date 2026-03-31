import random

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ace_conversion(card_list):
    total = sum(card_list)
    while total > 21:
        if 11 in card_list:
            card_list[card_list.index(11)] = 1
            total = sum(card_list)
        else:
            break
    return total

def blackjack():

    play_game = True

    while play_game:

        game_choice = input("do you want to play a game of black jack? type 'y' for yes and 'n' for no.\n")

        user_card = []

        computer_cards = []

        computer_total = 0

        if game_choice == "y":

            play_game = True

            print(art.logo)

            user_card.append(random.choice(cards))
            user_card.append(random.choice(cards))
            user_total = sum(user_card)

            while computer_total <= 16:
                computer_cards.append(random.choice(cards))
                ace_conversion(computer_cards)
                computer_total = ace_conversion(computer_cards)

            print(f"\nyour cards: {user_card}, current score: {user_total} \n")
            print(f"computer's cards: [{computer_cards[0]}], ?\n")

            hit_choice = "y"
            while hit_choice == "y":
                hit_choice = input("type 'y' to hit, or 'n' to stand. \n")
                user_total = user_total
                if hit_choice == "y":
                    user_card.append(random.choice(cards))
                    user_total = ace_conversion(user_card)

                    print(f"\nyour cards: {user_card}, current score: {user_total} \n")
                    print(f"computer's cards: [{computer_cards[0]}], ?\n")
                    hit_choice = "y"

                    if user_total > 21:
                        print(f"\nyour cards: {user_card}, current score: {user_total} \n")
                        print(f"computer's cards: {computer_cards}, computer score {computer_total}\n")
                        print("you bust, you lose.\n")
                        hit_choice = "n"

                else:
                    print(f"\nyour cards: {user_card}, current score: {user_total} \n")
                    print(f"computer's cards: {computer_cards}, computer score {computer_total}\n")

                    if user_total > 21:
                        print("you bust, you lose.")
                    elif computer_total > 21:
                        print("computer bust, you win.")
                    elif user_total > computer_total:
                        print("you win.")
                    elif user_total < computer_total:
                        print("you lose.")
                    elif user_total == computer_total:
                        print("push.")

                    hit_choice = "n"

        elif game_choice == "n":

            exit()

blackjack()
