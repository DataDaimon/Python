"""
Guess the Number
Richard Flores
December 28, 2022
"""

import random

print("\nWelcome to Guess the Number!")

lives = 0
mode = input("Choose Easy or Hard mode: ")
if mode == "easy":
    lives = 5
else:
    lives == 10

number = random.randint(1, 100)
print(number)

guess = int(input("\nEnter a guess: "))

def check_guess(int_guess, int_number):
    if guess > number:
        print("Too High!")
        return lives - 1
    elif guess < number:
        print("Too Low!")
        return lives - 1
    else:
        print("Winner! Winner! Chicken Dinner!")

check_guess(guess, number)
print(lives)

