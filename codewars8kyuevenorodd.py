#https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python
'''
Even or Odd

Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
'''

def even_or_odd(number):
    number = int(number)
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(5)) #print Odd
print(even_or_odd(-5)) #print Odd
print(even_or_odd(0)) #print Even
print(even_or_odd(-2)) #print Even
print(even_or_odd(2)) #print Even
