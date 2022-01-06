from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()


def have_coffee():
    items = menu.get_items()
    choice = input(f"What would you like? ({items}) :")

    drink_is_valid = menu.find_drink(choice)
    if choice == "report":
        coffee.report()
        money.report()
        have_coffee()

    else:
        if choice == "off":
            return
        if drink_is_valid:
            if coffee.is_resource_sufficient(drink_is_valid):
                if money.make_payment(drink_is_valid.cost):
                    coffee.make_coffee(drink_is_valid)
                    have_coffee()
                else:
                    have_coffee()


have_coffee()
