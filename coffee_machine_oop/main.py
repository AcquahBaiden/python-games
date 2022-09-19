from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffeeMaker = CoffeeMaker()
is_on = True

while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino):')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffeeMaker.report()
    else:
        menu = Menu()
        print(menu.get_items().find(choice))
        options = menu.get_items()
        if menu.get_items().find(choice):
            print('it is inside here')