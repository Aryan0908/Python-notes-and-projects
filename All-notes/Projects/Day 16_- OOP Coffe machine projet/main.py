from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = Menu()
coffee_info = CoffeeMaker()
money_info = MoneyMachine()

user_choice = True
while user_choice:
    user_input = input(f"Which coffee do you wish to have? ({coffee.get_items()})")
    if user_input != "report":
        drink = coffee.find_drink(user_input)

    if user_input == "report":
        coffee_info.report()
        money_info.report()

    elif coffee_info.is_resource_sufficient(drink):


        money_info.make_payment(drink.cost)
        coffee_info.make_coffee(drink)

