#https://www.codewars.com/kata/55d1d6d5955ec6365400006d/train/python
'''
Round up to the next multiple of 5 7kyu

Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?

Examples:

input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.

Input may be any positive or negative integer (including 0).

You can assume that all inputs are valid integers.
'''
def round_to_next5(n):
    while True:
        if n % 5 == 0:
            return n
        else:
            n += 1


print(round_to_next5(0)) #print 0
print(round_to_next5(2)) #print 5
print(round_to_next5(3)) #print 5
print(round_to_next5(12)) #print 15
print(round_to_next5(21)) #print 25
print(round_to_next5(30)) #print 35
print(round_to_next5(-2)) #print 0
print(round_to_next5(-5)) #print -5

#User submissions
import math

def round_to_next5(n):
    return math.ceil(n / 5.0) * 5
