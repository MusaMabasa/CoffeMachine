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
def process_coin():
    """Return total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters? $: ")) * 0.25
    total += int(input("How many dimes? $: ")) * 0.1
    total += int(input("How many pennies? $: ")) * 0.01
    return total

def drink(customer_order):
    drink = MENU[customer_order]
    print(drink)


def check_resource(drink):
    current_water = water - drink[water]
    print(current_water)


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry no enough {item}")
            return False
    return True

profit = 0
is_on = True
while is_on:
    print("Welcome to DaMoose Coffee vending machine")

    customer_order = input("What would you like to drink today (espresso/latte/Cappuccino)? ").lower()

    # TODO 2. Check if resources are enough order another drink
    if customer_order == "off":
        print("Machine is shutting down")
        is_on = False

    elif customer_order == "report":
        print(f"Your water is {resources['water']}ml")
        print(f"Your Milk is {resources['milk']}ml")
        print(f"Your Coffee is {resources['coffee']}g")

    else:
        drink = MENU[customer_order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if payment < drink["cost"]:
                print("Sorry that's not enough money. Money refunded")
            else:
                if payment >= drink["cost"]:
                    process_coin()


    # TODO 3. Check resources are sufficient.
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

