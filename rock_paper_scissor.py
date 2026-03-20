import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]

move_player = int(input("rock, paper, scissor, shoot! enter 0 for rock, 1 for paper, and 2 for scissors.\n"))

if move_player >= 0 and move_player <= 2:
    print(moves[move_player])

move_cpu = random.randint(0,2)

print("the computer chose")
print(moves[move_cpu])

if move_player >=3 or move_player < 0:
    print("your move is invalid start over.")
elif move_player == 0 and move_cpu == 2:
    print("you win.")
elif move_player == 1 and move_cpu == 0:
    print("you win")
elif move_player == 2 and move_cpu == 1:
    print("you win")
elif move_cpu == move_player:
    print("it's a draw")
else:
    print("you lose.")

