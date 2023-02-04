from art4 import logo
from art4 import vs
from game_data import data
import random

# print(data[random_int])
# print(data[1]['name'])
# print(data[1]['follower_count'])
player_score = 0

game_over = False

while not game_over:
    print(logo)
    random_int = random.randint(0, 49)

    random_int2 = random.randint(0, 49)

    print(f"Compare A: {data[random_int]['name']}, {data[random_int]['description']}, {data[random_int]['country']}.")
    print(vs)
    print(f"Compare B: {data[random_int2]['name']}, {data[random_int2]['description']}, {data[random_int2]['country']}.")
    player_choice = input("Who has more Followers? Type 'A' or 'B': ")

    random_a = data[random_int]['follower_count']
    random_b = data[random_int2]['follower_count']

    print(f"DEBUG A: {random_a}, B: {random_b}")

    if player_choice == 'A' and random_a > random_b:
        player_score = player_score + 1
        print(f"Correct! Player Score: {player_score}")
    elif player_choice == 'B' and random_b > random_a:
        player_score = player_score + 1
        print(f"Correct! Player Score: {player_score}")
    else:
        print(f"Game Over! Player Score: {player_score}")
        game_over = True
