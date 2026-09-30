#https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python
'''
Calculate BMI 8 kyu

Write function bmi that calculates body mass index (bmi = weight / height^2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
'''
def bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"


print(bmi(50, 1.80)) #print Underweight
print(bmi(80, 1.80)) #print Normal
print(bmi(90, 1.80)) #print Overweight
print(bmi(100, 1.80)) #print Obese
