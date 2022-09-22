rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

from random import randrange

print("\nRock, Paper, Scissors!")

choice = int(input("Enter 0 for Rock, 1 for Paper, or 2 for scissors: "))
pc_choice = randrange(1,3)

# print("\nPlayer Choice: " + str(choice))
# print("Computer Choice: " + str(pc_choice))

rps = ["rock", "paper", "scissors"]

print("\nYou chose: " + rps[choice])
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose: " + rps[pc_choice])
if pc_choice == 0:
    print(rock)
elif pc_choice == 1:
    print(paper)
else:
    print(scissors)

if choice == 0 and pc_choice == 2:
    print("You win! Rock beats scissors!")
elif choice == 1 and pc_choice == 0:
    print("You win! Paper beats Rock!")
elif choice == 2 and pc_choice == 1:
    print("You win! Scissors beats Paper")
elif choice == pc_choice:
    print("Tie game, try again!")
else:
    print("Computer wins.")