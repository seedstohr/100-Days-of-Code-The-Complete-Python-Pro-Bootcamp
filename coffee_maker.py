import sys

cash = float(0)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report_resources():
    """prints the current resources in the machine"""
    for s in resources:
        if s != "coffee":
            print(f"{s}: {resources[s]} ml")
        else:
            print(f"{s}: {resources[s]} g\n"
                  f"Money: ${cash}")

def menu_system():
    """menu system for coffee machine with secret report and secret off"""
    while True:
        user_choice_one = input("What would you like? (latte, espresso, cappuccino)\n")
        if user_choice_one == "off":
            sys.exit()
        elif user_choice_one == "report":
            report_resources()
        elif user_choice_one == "espresso":
            if resource_check(user_choice_one):
                payment(user_choice_one)
        elif user_choice_one == "latte":
            if resource_check(user_choice_one):
                payment(user_choice_one)
        elif user_choice_one == "cappuccino":
            if resource_check(user_choice_one):
                payment(user_choice_one)
        else:
            print("Invalid option, please try again.\n")

def resource_check(user_choice):
    """check resources was chosen drink"""
    if resources["water"] < MENU[user_choice]["ingredients"]["water"]:
        print(f"We do not have enough water to make a {user_choice}.\n")
        return False
    if resources["coffee"] < MENU[user_choice]["ingredients"]["coffee"]:
        print(f"We do not have enough coffee to make a(n) {user_choice}.\n")
        return False
    if "milk" in MENU[user_choice]["ingredients"]:
        if resources["milk"] < MENU[user_choice]["ingredients"]["milk"]:
            print(f"We do not have enough milk to make a(n) {user_choice}.\n")
            return False
    return True

def payment(user_choice):
    print(f"Your beverage cost ${MENU[user_choice]['cost']}\n"
          f"Please insert coins.")
    beverage_cost = float(MENU[user_choice]["cost"])
    quarters = int(input("How many quarters?\n"))
    dimes = int(input("How many dimes?\n"))
    nickles = int(input("How many nickles?\n"))
    pennies = int(input("How many pennies?\n"))
    money_entered = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
    if money_entered >= beverage_cost:
        global cash
        cash += beverage_cost
        resources["water"] = resources["water"] - MENU[user_choice]["ingredients"]["water"]
        if "milk" in MENU[user_choice]["ingredients"]:
            resources["milk"] = resources["milk"] - MENU[user_choice]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]
        change_owed = round(money_entered - beverage_cost, 2)
        print(f"Your change is ${change_owed}\n"
              f"Enjoy your {user_choice}")
    else:
        print("That was not enough. Money refunded. Try again.")

menu_system()

