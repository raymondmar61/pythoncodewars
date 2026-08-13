#https://www.codewars.com/kata/535474308bb336c9980006f2/train/python
'''
Greet Me 7 kyu

Write a method that takes one argument as name and then greets that name, capitalized and ends with an exclamation point.

Example:

"riley" --> "Hello Riley!"
"JACK"  --> "Hello Jack!"
'''
def greet(name):
    return f"Hello {name.capitalize()}!"


print(greet('riley')) #print Hello Riley!
print(greet('molly')) #print Hello Molly!
print(greet('BILLY')) #print Hello Billy!

addhello = "riley"
print(f"Hello {addhello.capitalize()}!") #print Hello Riley!
