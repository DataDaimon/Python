from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print("Welcome to Hotspresso!")

coffee_machine_power = True

while coffee_machine_power:
    customer_choice = input('What would you like? (espresso/latte/cappuccino): ')

    if customer_choice == "report":
        print('\nCurrent Resources: ')
        coffee_maker.report()
        money_machine.report()
        print('\n')
    elif customer_choice == 'off':
        coffee_machine_power = False
    else:
        drink = coffee_menu.find_drink(customer_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print('Not enough resources')