from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def menu_system():
    """menu system for coffee machine with secret report and secret off"""
    while True:
        user_choice_one = input(f"What would you like? {menu.get_items()}\n")
        if user_choice_one == "off":
            return False
        elif user_choice_one == "report":
            coffee_maker.report()
            money_machine.report()
        elif user_choice_one == "espresso":
            drink = menu.find_drink(user_choice_one)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        elif user_choice_one == "latte":
            drink = menu.find_drink(user_choice_one)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        elif user_choice_one == "cappuccino":
            drink = menu.find_drink(user_choice_one)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            print("Invalid option, please try again.\n")

menu_system()

