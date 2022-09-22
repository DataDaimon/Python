# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total = 0
counter = 0

for h in student_heights:
  total += h
  counter += 1

print("\nSum of Heights: " + str(total))
print("Number of Heights counted: "+ str(counter))

avg = total / counter
print("Calculated mean: " + str(avg))

