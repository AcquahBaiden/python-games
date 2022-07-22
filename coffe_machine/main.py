from decimal import Rounded


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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    """Prints the resources and amount remaining"""
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: {profit}')


def process_coins():
    """Receives coins and returns Total inserted"""
    quarters = input("How many quarters?")
    dimes = input("How many dimes?")
    nickles = input("How many nickles?")
    pennies = input("How many pennies?")

    total = (int(quarters) * 0.25) + (int(dimes) * 0.10) + (int(nickles) * 0.05) + (int(pennies) * 0.01)
    return total


def is_transaction_successful(amount_received, drink_cost):
    """Returns True when the payment amount is accept and False if money is insufficient"""
    if amount_received >= drink_cost:
        change = round(amount_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry money is insufficient. Money refunded")
        return False


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("Sorry there is not enough water")
            return False
    return True


def update_resources(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]


is_on = True

while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino):')
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])
            update_resources(drink["ingredients"])
        else:
            print("Sorry your money is insufficient")

