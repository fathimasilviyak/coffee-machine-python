# TODO 1. import MENU and resources from data.
from data import MENU, resources
menu = MENU

# TODO 5: Function to check resources is sufficient
def is_resource_sufficient(ingredients):
    """Return True if ingredients are sufficient else return false."""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True


# TODO 6: Function to process coin
def process_coins():
    """Returns the total value of coins in dollar."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


# TODO 7: Check transaction is successful
def is_transaction_successful(payment, cost):
    """Return True if payment is sufficient, else return False"""
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO 8. Make coffee
def make_coffee(drink_name, required_ingredients):
    """If the transaction is successful, then deduct the required ingredients from the resources"""
    for item in required_ingredients:
        resources[item] -= required_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


is_coffee_machine_on = True
profit = 0

while is_coffee_machine_on:
    # TODO 2. Ask user to choose the type of coffee he want.
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO 3. Turn off the Coffee Machine if the input is “off”.
    if user_input == "off":
        is_coffee_machine_on = False
    # TODO 4. print the report.
    elif user_input == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")

    else:
        user_coffee = menu[user_input]
        if is_resource_sufficient(user_coffee["ingredients"]):
            paid_amount = process_coins()
            if is_transaction_successful(paid_amount, user_coffee['cost']):
                make_coffee(user_input, user_coffee['ingredients'])
