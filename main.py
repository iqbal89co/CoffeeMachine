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

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

money = 0.0


# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappucino):"
# TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt

# TODO: 3. Print report
# TODO: 4. Check resources sufficient
# TODO: 5. Process coins if user prompts enough coins


def check_sufficient(coffee_name):
    for resource, value in resources.items():
        menu_resource = MENU.get(coffee_name, {}).get("ingredients", {}).get(resource, 0)
        if value >= menu_resource:
            continue
        else:
            print("Sorry there is not enough " + resource)
            return False
    return True


def input_coins():
    quarters = float(input("add quarters: "))
    dimes = float(input("add dimes: "))
    nickles = float(input("add nickles: "))
    pennies = float(input("add pennies: "))
    total_coins = quarters * coins["quarters"] + dimes * coins["dimes"] + nickles * coins["nickles"] + pennies * coins[
        "pennies"]
    return total_coins


def subtract_coffee_price(coffee_name, total_coins):
    return total_coins - MENU[coffee_name]["cost"]


# TODO: 7. Make Coffee
# Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”
def make_coffee(coffee_name):
    for resource, value in resources.items():
        resources[resource] -= MENU.get(coffee_name, {}).get("ingredients", {}).get(resource, 0)
    print("Here is your latte. Enjoy!")
    return


def check_input(coffee_input):
    global money
    if coffee_input == "report":
        for resource, value in resources.items():
            print(resource + ": " + str(value))
        print("money: $" + str(money))
    elif MENU.get(coffee_input, -1) != -1:
        if check_sufficient(coffee_input):
            # TODO: 6. Check transaction successful
            # if user not inserted enough money program should say  “Sorry that's not enough money. Money refunded.”
            # if user has inserted too much money, the machine should offer change.
            # E.g. “Here is $2.45 dollars in change.”
            total_coins = input_coins()
            transaction = subtract_coffee_price(coffee_input, total_coins)
            if transaction < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money += MENU[coffee_input]["cost"]
                print("Here is $" + str("{:.2f}".format(transaction)) + " dollars in change.")
                make_coffee(coffee_input)
        return
    else:
        print("invalid input")
    return


coffee = "on"

while coffee != "off":
    coffee = input("What would you like? (espresso/latte/cappuccino):")
    check_input(coffee)
print("see you again!")
