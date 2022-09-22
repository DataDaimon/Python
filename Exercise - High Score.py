# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores: ").split(",")
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# 78 65 89 86 55 91 64 89

high_score = 0

for score in student_scores:
  if score > high_score:
    high_score = score

print("The high score is: " + str(high_score))


