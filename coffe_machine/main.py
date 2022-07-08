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
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: {profit}')


def receive_coins(drink_info):
    is_transaction_successful = False;
    quarters = input("How many quarters?")
    dimes = input("How many dimes?")
    nickles = input("How many nickles?")
    pennies = input("How many pennies?")

    total = (int(quarters) * 0.25) + (int(dimes) * 0.10) + (int(nickles) * 0.05) + (int(pennies) * 0.01)
    if total > drink["cost"]:
        print(f"Here is ${total - drink_info['cost']:.2f} in change")
        is_transaction_successful = True
    elif total < drink_info["cost"]:
        print("You don't have enough money. Money refunded")
    elif total == drink_info["cost"]:
        print("No need to give you any change")
        is_transaction_successful = True
    return is_transaction_successful


def check_resources_sufficient(drink):
    if drink["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water")
        return False
    elif drink["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk")
        return False
    elif drink["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough milk")
        return False
    else:
        return receive_coins(drink)


def update_resources(ingredients):
    resources["water"] -= ingredients["water"]
    resources["milk"] -= ingredients["milk"]
    resources["coffee"] -= ingredients["coffee"]


is_on = True

while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino):')
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    else:
        drink = MENU[choice]
        is_success = check_resources_sufficient(drink)
        if is_success:
            update_resources(drink["ingredients"])


