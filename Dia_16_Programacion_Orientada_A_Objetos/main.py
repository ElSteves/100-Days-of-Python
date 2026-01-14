from turtledemo.chaos import coosys

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_make = CoffeeMaker()
money_thing = MoneyMachine()

choice = ""

while choice != "off":
    choice = input(f"What drink do you want? {menu.get_items()}: ")
    if choice == "report":
        coffe_make.report()
        money_thing.report()
    elif choice in menu.get_items():
        my_drink = menu.find_drink(choice)
        if coffe_make.is_resource_sufficient(my_drink) and money_thing.make_payment(my_drink.cost):
            coffe_make.make_coffee(my_drink)
    else:
        print("Escoja una opción disponible")


