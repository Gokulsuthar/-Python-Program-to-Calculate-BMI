# BMI calculator

import numpy as np

height = float(input("Height(m): "))
weight = float(input("Weight(kg): "))

bmi = weight / height * height
BMI = float(bmi)

category = ["Underweight", "Normal weight", "Overweight", "Obesity"]

if BMI <= 18.4:
    print("BMI: ",BMI,"(You are underweight)")
elif BMI <= 24.9:
    print("BMI: ",BMI,"(You are healthy)")
elif BMI <= 29.9:
    print("BMI",BMI,"(You are over weight)")
elif BMI <= 34.9:
    print("BMI: ",BMI,"(You are severely over weight)")
elif BMI <= 39.9:
    print("BMI: ",BMI,"(You are obese)")
else:
    print("BMI: ",BMI,"(You are severely obese)")