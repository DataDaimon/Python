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

p_hand = [p_card1, p_card2]
d_hand = [d_card1, d_card2]

p_total = p_card1 + p_card2
d_total = d_card1 + d_card2

print("\nWelcome to BlackJack Casino!\n")

print("Your hand:")
print(f" [{p_card1}] [{p_card2}]")
print(f"Total: {p_total}")

print("\nDealer's Hand: ")
print(f" [{d_card1}] [{d_card2}]")
print(f"Total: {d_total}")

game_over = False

while not game_over:
    p_choice = input("\nHit or Stand: ")

    if p_choice == "hit":
        p_card3 = rand_card()
        p_hand.append(p_card3)
        p_total += p_card3
        print(p_hand)
        print(f"Total: {p_total}")

    if p_total > 21:
        print("Bust!")
        game_over = True

    if p_choice == "stand":
        while d_total < 17:
            d_card3 = rand_card()
            d_hand.append(d_card3)
            d_total += d_card3

        if d_total >= p_total:
            print(f"Dealer: {d_total}, Player: {p_total}")
            print("Dealer wins")
            game_over = True
        else:
            print(f"Dealer: {d_total}, Player: {p_total}")
            print("You win!")
            game_over = True