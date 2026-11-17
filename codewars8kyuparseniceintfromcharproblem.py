#https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1/train/python
'''
Parse nice int from char problem 8 kyu

You ask a small girl "How old are you?" She always says "x years old", where x is a random number between 0 and 9.

Write a program that returns the girl's age (0-9) as an integer.

Assume the test input string is always a valid string. For example, the test input may be "1 year old" or "5 years old". The first character in the string is always a number.
'''
def get_age(age):
    return int(age[0])


print(get_age("2 years old")) #print 2
print(get_age("4 years old")) #print 4
print(get_age("5 years old")) #print 5
print(get_age("7 years old")) #print 7
print(get_age("1 year old")) #print 1
print(get_age("0 year old")) #print 0
