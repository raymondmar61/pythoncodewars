#https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python
'''
Opposite number 8kyu

Very simple, given a number, find its opposite (additive inverse).

Examples:

1: -1
14: -14
-34: 34
'''
def opposite(number):
    return number * -1


print(opposite(1)) #print -1
print(opposite(25.6)) #print -25.6
print(opposite(0)) #print 0
print(opposite(1425.2222)) #print -1425.2222
print(opposite(-3.1458)) #print 3.1458
print(opposite(-95858588225)) #print 95858588225

#User solution
def opposite(number):
    return -number
