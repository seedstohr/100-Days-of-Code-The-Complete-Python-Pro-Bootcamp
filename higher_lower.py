#import game_data randint and art
from random import randint
import game_data
import art

#initialize answer
answer = ""
#initialize user_score
user_score = 0
#initialize user_choice
user_choice = ""

def random_entry():
    """return random int based on data length"""
    entry = randint(0, len(game_data.data) -1)
    return entry

def compare_followers():
    """compare follower counts of person_a to person_b and return 'a' or 'b' as 'answer'"""
    if game_data.data[person_a]['follower_count'] > game_data.data[person_b]['follower_count']:
        answer = "a"
    elif game_data.data[person_a]['follower_count'] < game_data.data[person_b]['follower_count']:
        answer = "b"
    return answer

person_a = random_entry()
person_b = random_entry()
while person_b == person_a:
    person_b = random_entry()

while answer == user_choice:

    answer = compare_followers()
    print(art.logo)
    print(f"Current Score: {user_score}")
    print(f"Compare A: {game_data.data[person_a]['name']}, a {game_data.data[person_a]['description']}, "
          f"from {game_data.data[person_a]['country']}.")
    print(art.vs)
    print(f"Compare B: {game_data.data[person_b]['name']}, a {game_data.data[person_b]['description']}, "
          f"from {game_data.data[person_b]['country']}.\n")
    user_choice = input("Who has more followers? Type 'A' or 'B':\n").lower()
    if user_choice == answer:
        user_score += 1
        if answer == "b":
            person_a = person_b
        person_b = random_entry()
        while person_b == person_a:
            person_b = random_entry()
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {user_score}")
