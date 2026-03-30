import art

print(art.logo)

user_bids = {}

def bids():
    more_bids = True
    while more_bids:
        person = input("What is you name?\n")
        bid = int(input("What is your bid?\n"))
        user_bids[person] = bid
        answer =input("Are there more bidders?\n")
        if answer == "no":
            more_bids = False
        else:
            print("\n" * 200)
bids()

highest_bid = 0
winner = ""

for bidders in user_bids:
    if user_bids[bidders] > highest_bid:
        highest_bid = user_bids[bidders]
        winner = bidders

print(f"The winner is {winner} with bids {highest_bid}")
