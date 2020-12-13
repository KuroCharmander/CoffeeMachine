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


def report(money):
    """Report the amount of resources in the coffee machine."""
    print(f"    Water: {resources['water']}ml \n"
          f"    Milk: {resources['milk']}ml \n"
          f"    Coffee: {resources['coffee']}g \n"
          f"    Money: ${money:.2f}")


def check_resources(drink_name):
    """Returns true if there is enough resources in the coffee machine to make the drink."""
    drink = MENU[drink_name]
    is_enough = True
    for ingredient in drink["ingredients"]:
        if resources[ingredient] < drink["ingredients"][ingredient]:
            print(f"    Sorry, there is not enough {ingredient}.")
            is_enough = False
    return is_enough


def process_coins():
    """Process the coins that are inputted."""
    print("    Please insert coins.")
    return int(input("    How many quarters?: ")) * 0.25 \
        + int(input("    How many dimes?: ")) * 0.1 \
        + int(input("    How many nickels?: ")) * 0.05 \
        + int(input("    How many pennies?: ")) * 0.01


def transaction(paid, drink_name):
    """Returns cost of the drink or 0 if there is not enough money to pay for the drink."""
    drink_cost = MENU[drink_name]["cost"]
    if paid < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return 0
    else:
        if paid != drink_cost:
            print(f"Here is ${(paid - drink_cost):.2f} in change.")
        make_coffee(drink_name)
        return drink_cost


def make_coffee(drink_name):
    """Makes the drink and uses the ingredients in the coffee machine according to the menu."""
    drink = MENU[drink_name]
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]
    print(f"Here is your {drink_name}. Enjoy!")


def coffee_machine():
    """A coffee machine that dispenses a drink."""
    money = 0
    operational = True
    while operational:
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        if drink == "off":
            operational = False
        elif drink == "report":
            report(money)
        elif drink in MENU:
            is_sufficient = check_resources(drink)
            if is_sufficient:
                money += transaction(process_coins(), drink)
        else:
            print("Sorry, that is not an option. Please try again.")


coffee_machine()
