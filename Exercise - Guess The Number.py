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
    lives = 10
else:
    lives = 5

number = random.randint(1, 100)
print(number)

game_over = False

while not game_over:
    guess = int(input("\nEnter a guess: "))

    def check_guess(int_guess, int_number):
        global lives
        global game_over
        if guess > number:
            print("Too High!")
            lives = lives - 1
        elif guess < number:
            print("Too Low!")
            lives = lives - 1
        else:
            print("Winner! Winner! Chicken Dinner!")
            game_over = True

    check_guess(guess, number)
    print(f"You have {lives} lives left.")
    if lives == 0:
        print(f"No lives left, Game Over.")
        game_over = True


