#https://www.codewars.com/kata/5748838ce2fab90b86001b1a/train/python
'''
Area of a Square 8 kyu

Complete the function that calculates the area of the red square, when the length of the circular arc A is given as the input. #RM:  there is an image.

Note: use the π value provided in your language (Math::PI, M_PI, math.pi, etc)
'''
from math import pi
def square_area(a):
    return (4 * pow(a, 2)) / pow(pi, 2)


print(square_area(2)) #print 1.6211389382774044
print(square_area(0)) #print 0.0
print(square_area(14.05)) #print 80.00421981582633
print(square_area(1)) #print 0.4052847345693511
print(square_area(100)) #print 4052.8473456935108

from math import pi
aarc = 14.05
print(pi) #print 3.141592653589793
print((4 * pow(aarc, 2)) / pow(pi, 2)) #print 80.00421981582635

#User solution
def square_area(A):
    return round((2 * A / pi) ** 2, 2)