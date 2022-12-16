"""
BlackJack
Richard Flores
12/16/2022
"""

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def rand_card():
    new_card = random.choice(cards)
    return new_card


p_card1 = rand_card()
p_card2 = rand_card()

d_card1 = rand_card()
d_card2 = rand_card()

print("\nWelcome to BlackJack Casino\n")

print("Your hand:")
print(f" [{p_card1}] [{p_card2}]")
print("Total: ")

print("\nDealer's Hand: ")
print(f" [{d_card1}] [{d_card2}]")
print("Total: ")



