"""
Simple Calculator
Richard Flores
12/15/2020
"""

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("Enter a number: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Choose an operation: ")
num2 = int(input("Enter second a number: "))
calc_func = operations[operation_symbol]
answer = calc_func(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
continue_game = input("Continue Calculation (Y or N): ")

game_over = True

while game_over:
    if continue_game == "n":
        game_over = False
    else:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Choose an operation: ")
        num3 = int(input("Enter a new number: "))
        calc_func = operations[operation_symbol]
        prev_answer = answer
        answer = calc_func(answer, num3)
        print(f"{prev_answer} {operation_symbol} {num3} = {answer}")
        continue_game = input("Continue Calculation (Y or N): ")
        if continue_game == "n":
            game_over = False