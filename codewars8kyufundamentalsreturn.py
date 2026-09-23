#https://www.codewars.com/kata/55a5befdf16499bffb00007b/train/python
'''
Fundamentals: Return 8 kyu

Make multiple functions that will return the sum, difference, modulus, product, quotient, and the exponent respectively.

Please use the following function names:

addition = add

multiply = multiply

division = divide (both integer and float divisions are accepted)

modulus = mod

exponential = exponent

subtraction = subt
'''
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def mod(a, b):
    return a % b

def exponent(a, b):
    return a**b

def subt(a, b):
    return a - b


print(add(1, 2)) #print 3
print(multiply(1, 2)) #print 2
print(divide(2, 1)) #print 2
print(mod(1, 2)) #print 1
print(exponent(1, 2)) #print 1
print(subt(1, 2)) #print -1
