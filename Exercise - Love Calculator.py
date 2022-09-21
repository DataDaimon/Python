# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

fullname = name1 + name2

true_score = 0
love_score = 0

true_score += fullname.count("t")
true_score += fullname.count("r")
true_score += fullname.count("u")
true_score += fullname.count("e")

love_score += fullname.count("l")
love_score += fullname.count("o")
love_score += fullname.count("v")
love_score += fullname.count("e")

print(f"\nTrue Score: {true_score}")
print(f"Love Score: {love_score}")

final_score = str(true_score) + str(love_score)
final_score = int(final_score)

if final_score <= 10 or final_score >= 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"\nFinal Score: {final_score}")



