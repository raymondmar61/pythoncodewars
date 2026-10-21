#https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/train/python
'''
Quarter of the year 8 kyu

Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

Constraint:

1 <= month <= 12
'''
def quarter_of(month):
    if month >= 1 and month <= 3:
        return 1
    elif month >= 4 and month <= 6:
        return 2
    elif month >= 7 and month <= 9:
        return 3
    elif month >= 10 and month <= 12:
        return 4


print(quarter_of(3)) #print 1
print(quarter_of(8)) #print 3
print(quarter_of(11)) #print 4

#User solution
def quarter_of(month):
    # your code here
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4
