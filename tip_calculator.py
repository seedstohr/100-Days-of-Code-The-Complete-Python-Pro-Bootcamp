#welcome the user
print("Welcome to the tip calculator!")
#ask the for the bills amount
bill = float(input("What was the total bill? $"))
#ask for the amount they want to tip
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
#ask for number of people splitting the bill
people = int(input("How many people to split the bill? "))
#calculate the amount per person
cost = round((bill / people) * ((tip / 100) + 1 ), 2)
#print the amount owed
print(f"Each person should pay ${cost}")

