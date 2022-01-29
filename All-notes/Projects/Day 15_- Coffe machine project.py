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
    "ingredients": {"water": 300,
                    "milk": 200,
                    "coffee": 100, },
    "coins": 0
}


def requirement(coffee_resources, total_resources):
    if coffee_resources["water"] < total_resources["water"]:
        if coffee_resources["milk"] < total_resources["milk"]:
            if coffee_resources["coffee"] < total_resources["coffee"]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def payment(coffee_cost):
    pennies = 0.01
    nickles = 0.05
    dimes = 0.10
    quarters = 0.25

    num_quarters = int(input("How many quarters? : "))
    num_dimes = int(input("How many dimes? : "))
    num_nickles = int(input("How many nickles? : "))
    num_pennies = int(input("How many pennies? : "))

    total_payment = (num_quarters * quarters) + (num_dimes * dimes) + (num_nickles * nickles) + (num_pennies * pennies)

    if total_payment > coffee_cost:
        return f"Here is your change: ${total_payment - coffee_cost}\nEnjoy your coffee!"
    elif total_payment < coffee_cost:
        return "Sorry, that's not enough money. Money Refunded."
    else:
        return "Enjoy your coffee!"


def report(resource_input):
    water = resource_input["ingredients"]["water"]
    milk = resource_input["ingredients"]["milk"]
    coffee = resource_input["ingredients"]["coffee"]
    coins = resource_input["coins"]
    print(f"Water = {water}")
    print(f"Milk = {milk}")
    print(f"Coffee = {coffee}")
    print(f"Coins = {coins}")


user_choice = True

while user_choice:

    user_input = input("What would you like to have? (espresso/latte/cappuccino) ")

    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":

        resources_water = resources["ingredients"]["water"]
        resources_milk = resources["ingredients"]["milk"]
        resources_coffee = resources['ingredients']["coffee"]

        user_input_water = MENU[user_input]["ingredients"]["water"]
        user_input_milk = MENU[user_input]["ingredients"]["milk"]
        user_input_coffee = MENU[user_input]["ingredients"]["coffee"]
        cost = MENU[user_input]["cost"]

        requirement_fulfill = requirement(coffee_resources=MENU[user_input]["ingredients"],
                                          total_resources=resources["ingredients"])

        if requirement_fulfill:
            print("Please insert coins")
            print(payment(coffee_cost=cost))

            resources["ingredients"]["water"] = resources_water - user_input_water
            resources["ingredients"]["milk"] = resources_milk - user_input_milk
            resources["ingredients"]["coffee"] = resources_coffee - user_input_coffee
            resources["coins"] += cost

        else:
            unavailable_resources = ""

            for left_resources in resources["ingredients"]:
                current_resources = resources["ingredients"][left_resources]

                user_demand = MENU[user_input]["ingredients"][left_resources]
                if user_demand > current_resources:
                    unavailable_resources += left_resources

            print(f"Sorry there is not enough, {unavailable_resources}")



    else:
        print(report(resources))
