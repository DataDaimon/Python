# 🚨 Don't change the code below 👇
import math

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / height**2
bmi = math.ceil(bmi)
bmi_output = ""

print(f"\nYour BMI is {bmi}")

if bmi < 18.5:
    bmi_output = "underweight"
elif bmi < 25:
    bmi_output = "normal weight"
elif bmi < 30:
    bmi_output = "slightly overweight"
elif bmi_output < 35:
    bmi_output = "obese"
else:
    bmi_output = "clinically obese"

print(f"Your calculated BMI is {bmi_output}")
