#Beginner Series #3 Sum of Numbers
#https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
'''
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

Your function should only return a number, not the explanation about how you get that number.
'''
a = 1
b = 2
if a > b:
    integersbetween = [x for x in range(b, a + 1)]
    print(sum(integersbetween))
else:
    integersbetween = [x for x in range(a, b + 1)]
    print(sum(integersbetween)) #print 3

def get_sum(a, b):
    if a == b:
        return a
    elif a > b:
        return sum([x for x in range(b, a + 1)])
    else:
        return sum([x for x in range(a, b + 1)])


print(get_sum(1, 0)) #print 1
print(get_sum(1, 2)) #print 3
print(get_sum(0, 1)) #print 1
print(get_sum(1, 1)) #print 1
print(get_sum(-1, 0)) #print -1
print(get_sum(1, 2)) #print 3
