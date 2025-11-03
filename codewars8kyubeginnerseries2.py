#https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python
'''
Beginner Series #2 Clock 8kyu

Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
'''
def past(h, m, s):
    h = h * 60 * 60
    m = m * 60
    totalmilliseconds = (h * 1000) + (m * 1000) + (s * 1000)
    return totalmilliseconds


print(past(0, 1, 1)) #print 61000
print(past(1, 1, 1)) #print 3661000
print(past(0, 0, 0)) #print 0
print(past(1, 0, 1)) #print 3601000
print(past(1, 0, 0)) #print 3600000

h, m, s = 1, 1, 1
hourstoseconds = h * 60 * 60
print(hourstoseconds) #print 3600
minutestoseconds = m * 60
print(minutestoseconds) #print 60
print(s) #print 1
totalmilliseconds = (hourstoseconds * 1000) + (minutestoseconds * 1000) + (s * 1000)
print(totalmilliseconds) #print 3661000
