#https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python
'''
Factorial 7 kyu
In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).

More details about factorial can be found here.
'''
import math
def factorial(n):
    if n < 0 or n > 12:
        raise ValueError("Range must be between 1 and 11")
    else:
        return math.factorial(n)


print(factorial(0)) #print 1
print(factorial(1)) #print 1
print(factorial(2)) #print 2
print(factorial(3)) #print 6

def factorialfunctionnomathmodule(n):
    answer = 1
    if n < 0 or n > 12:
        raise ValueError("Range must be between 1 and 11")
    else:
        for eachfactorial in range(n, 0, -1):
            answer = answer * eachfactorial
        return answer


print(factorialfunctionnomathmodule(0)) #print 1
print(factorialfunctionnomathmodule(1)) #print 1
print(factorialfunctionnomathmodule(2)) #print 2
print(factorialfunctionnomathmodule(3)) #print 6


factorial = 3
answer = 1
for eachfactorial in range(factorial, 0, -1):
    print(eachfactorial)
    answer = answer * eachfactorial
    print(answer)
    '''
    3
    3
    2
    6
    1
    6
    '''
number = 5
from math import factorial
print(factorial(number)) #print 120
number = -12
if number < 0 or number > 12:
    raise ValueError("Range must be between 1 and 11") #return ValueError: Range must be between 1 and 11
else:
    print(factorial(number))
number = 5
if number < 0 or number > 12:
    raise ValueError("Range must be between 1 and 11")
else:
    print(factorial(number))
