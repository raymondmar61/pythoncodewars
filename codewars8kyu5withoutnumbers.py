#https://www.codewars.com/kata/59441520102eaa25260000bf/train/python
'''
5 without numbers !! 8 kyu

Write a function that always returns 5

Sounds easy right? Just bear in mind that you can't use any of the following characters: 0123456789*+-/

Good luck :)

RM:  Return the number 5.  The code can't use all numbers.  The code can't use arithmetic opereations multiply, add, subtract, and divide.  Google research said no need to worry about input values to the unusual_five() function.
'''
def unusual_five():
    return len("fives")


print(unusual_five()) #print 5
