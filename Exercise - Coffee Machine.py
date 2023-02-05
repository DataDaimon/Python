# Coffee Machine Exercise
# Author: Richard Flores
# Date: 2023/02/05

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

profit = 0

def coffee_resources():
    print(f"RESOURCES \nWater: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']}\nMoney: ${profit}\n")

def check_resources(user_selection):
    if user_selection == 'espresso':
        if resources['water'] >= 50 and resources['coffee'] >= 18:
            payment(user_selection)
        else:
            print("Not Enough Resources!")
    elif user_selection == 'latte':
        if resources['water'] >= 200 and resources['milk'] >= 150 and resources['coffee'] >= 24:
            payment(user_selection)
        else:
            print("Not Enough Resources!")
    elif user_selection == 'cappuccino':
        if resources['water'] >= 250 and resources['milk'] >= 100 and resources['coffee'] >= 24:
            payment(user_selection)
        else:
            print("Not Enough Resources!")

def payment(user_selection):
    if user_selection == 'espresso':
        print("The cost is $1.50")
        change_machine(1.50)
    elif user_selection == 'latte':
        print("The cost is $2.50")
        change_machine(2.50)
    elif user_selection == 'cappuccino':
        print('The cost is $3.00')
        change_machine(3.00)

def change_machine(fee):
    global profit
    quarters = int(input('Enter number of Quarters: '))
    dimes = int(input('Enter number of Dimes: '))
    nickels = int(input('Enter number of Nickels: '))
    pennies = int(input('Enter number of Pennies: '))
    total_entered = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    print(f'Amount entered: ${total_entered}')
    if total_entered == fee:
        print(f'Dispensing {user_selection}')
        profit = profit + fee
        dispense_drink(user_selection)
    elif total_entered > fee:
        refund = total_entered - fee
        profit = profit + fee
        print(f'Dispensing {user_selection}. Your change is {refund}')
    else:
        print('Valid amount not entered.')

def dispense_drink(user_selection):
    if user_selection == 'espresso':
        resources['water'] -= 50
        resources['coffee'] -= 18
        print(f'Please enjoy your {user_selection}!\n')
    elif user_selection == 'latte':
        resources['water'] -= 200
        resources['milk'] -= 150
        resources['coffee'] -= 24
        print(f'Please enjoy your {user_selection}!\n')
    else:
        resources['water'] -= 250
        resources['milk'] -= 100
        resources['coffee'] -= 24
        print(f'Please enjoy your {user_selection}!\n')


coffee_machine_power = True

while coffee_machine_power:
    user_selection = input('What would you like? (espresso/latte/cappuccino): ')
    if user_selection == 'report':
        coffee_resources()
    elif user_selection == 'off':
        coffee_machine_power = False
    else:
        check_resources(user_selection)
