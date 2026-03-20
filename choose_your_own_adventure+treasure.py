print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input("you have come to a fork in the road, do you go left or right? ")
if choice == "left" or choice == "Left":
    choice = input("you come across a boggy marsh do you swim across or wait for a boat? ")
    if choice == "wait" or choice == "Wait":
        choice = input("across the marsh you come across three magical doors. one red, one blue and one yellow. Which do you go through? ")
        if choice == "red" or choice == "Red":
            print("a fire breathing geko lights your body on fire until it is nothing but a pile of smoldering ashes. game over.")
        elif choice == "blue" or choice == "Blue":
            print("you are swallowed by the dark abyss until you wither away to nothing. game over.")
        elif choice == "yellow" or choice == "Yellow":
            print("you have found a mystical land filled with treasure beyond measure. you win. ")
        else:
            print("you were paralyzed by fear and died from exposure. game over.")
    else:
        print("you are taken under by a manatee and boned to death. game over.")
else:
    print("you fall into a pit of spikes and slowly bleed out. game over.")
