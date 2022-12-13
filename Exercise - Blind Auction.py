import os
from art2 import logo

clear = lambda: os.system('cls')

print(logo)
print("Welcome to the blind auction program!")

bid_dict = {}
game_over = True

while game_over:
    name = str(input("Please enter your name: "))
    bid = int(input("Please enter your bid: "))
    bid_dict[name] = bid

    addl = input("Additional bids (yes or no): ")
    clear()
    if addl == "no":
        max_bid = max(bid_dict, key=bid_dict.get)
        print(f"\nThe winner is: {max_bid}")
        game_over = False
