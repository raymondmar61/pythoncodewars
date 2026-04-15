#https://www.codewars.com/kata/524f5125ad9c12894e00003f/train/python
'''
Find the Remainder 8 kyu
Task:
Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.

Division by zero should return an empty value.

Examples:
n = 17
m = 5
result = 2 (remainder of `17 / 5`)

n = 13
m = 72
result = 7 (remainder of `72 / 13`)

n = 0
m = -1
result = 0 (remainder of `0 / -1`)

n = 0
m = 1
result - division by zero (refer to the specifications on how to handle this in your language).  RM:  Python is ZeroDivisionError: integer division or modulo by zero

'''
def remainder(a, b):
    if (a == 0 and b > 0) or (b == 0 and a > 0) or (a == 0 and b == 0):
        # print("first if")
        return None
    elif a > b:
        # print("second if")
        return a % b
    elif b > a:
        # print("third if")
        return b % a
    elif a == b:
        return 0


print(remainder(17, 5)) #print 2
print(remainder(13, 72)) #print 7
print(remainder(0, -1)) #print 0
print(remainder(0, 1)) #print None
print(remainder(72, 13)) #print 7
print(remainder(1, 0)) #print None
print(remainder(0, 0)) #print None
print(remainder(0, 1)) #print None
print(remainder(-1, 0)) #print 0
print(remainder(0, -1)) #print 0
print(remainder(-13, -13)) #print 0
print(remainder(-60, 340)) #print -20
print(remainder(60, -40)) #print -20

print(17 % 5) #print 2
print(72 % 13) #print 7
print(0 % -1) #print 0
print(-13 % -13) #print 0
