import random
from random import randrange

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)
print(chosen_word)

guess = input("Guess a letter: ").lower()

answer_array = []
lives = 6

for letter in chosen_word:
    answer_array.append(" ")

while not chosen_word == answer_array:
    for n in range(0, len(chosen_word)):
        if chosen_word[n] == guess:
            answer_array[n] = guess
    print(answer_array)
    if lives == 0:
        print("Game Over")
        break
    elif chosen_word != answer_array:
        guess = input("Guess a letter: ").lower()
        lives -= 1
        print(lives)

    else:
        break



