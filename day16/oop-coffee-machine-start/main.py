from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def run_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    stop = False

    while not stop:
        selection = input("Please select a drink latte/espresso/cappuccino: ")
        if selection == 'report':
            coffee_maker.report()
            money_machine.report()
        if selection == 'off':
            stop = True
            print("Turning off.")
        if selection in ["espresso", "latte", "cappuccino"]:
            selected_item = menu.find_drink(selection)
            if coffee_maker.is_resource_sufficient(selected_item):
                if money_machine.make_payment(selected_item.cost):
                    coffee_maker.make_coffee(selected_item)


run_machine()
