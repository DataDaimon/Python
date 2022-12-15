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
num2 = int(input("Enter second a number: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Choose an operation: ")



print(f"{num1} {operation_symbol} {num2} = {answer}")
