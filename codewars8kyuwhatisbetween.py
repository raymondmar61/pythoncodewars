#https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/python
'''
What is between? 8kyu

Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

For example:

a = 1
b = 4
--> [1, 2, 3, 4]
'''
def between(a, b):
    return list(range(a, b + 1))


print(between(1, 4)) #print [1, 2, 3, 4]
print(between(-2, 2)) #print [-2, -1, 0, 1, 2]

a = 1
b = 4
print(list(range(a, b + 1))) #print [1, 2, 3, 4]
