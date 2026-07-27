#https://www.codewars.com/kata/56170e844da7c6f647000063/train/python
'''
Drink about 8 kyu

Kids drink toddy.
Teens drink coke.
Young adults drink beer.
Adults drink whisky.
Make a function that receive age, and return what they drink.

Rules:

Children under 14 old.
Teens under 18 old.
Young under 21 old.
Adults have 21 or more.
Examples: (Input --> Output)

13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"
'''
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    elif age >= 21:
        return "drink whisky"
    else:
        return "error"


print(people_with_age_drink(13)) #print drink toddy
print(people_with_age_drink(0)) #print drink toddy
print(people_with_age_drink(17)) #print drink coke
print(people_with_age_drink(15)) #print drink coke
print(people_with_age_drink(14)) #print drink coke
print(people_with_age_drink(20)) #print drink beer
print(people_with_age_drink(18)) #print drink beer
print(people_with_age_drink(22)) #print drink whisky
print(people_with_age_drink(21)) #print drink whisky
print(people_with_age_drink(30)) #print drink whisky


age = 13
if age < 14:
    print("drink toddy") #print toddy
elif age < 18:
    print("drink coke")
elif age < 21:
    print("drink beer")
elif age >= 21:
    print("drink whisky")
