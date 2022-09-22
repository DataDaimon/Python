# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

print(position[0] + " First Number")
print(position[1] + " Second Number")
first = int(position[0])
second = int(position[1])
first -= 1

if second == 1:
    row1[first] = "  X  "
elif second == 2:
    row2[first] = "  X  "
elif second == 3:
    row3[first] = "  X  "

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")