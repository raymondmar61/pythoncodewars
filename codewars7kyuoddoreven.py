#https://www.codewars.com/kata/5949481f86420f59480000e7/train/python
'''
Odd or Even? 7 kyu

Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).

Examples:
Input: [0]
Output: "even"

Input: [0, 1, 4]
Output: "odd"

Input: [0, -1, -5]
Output: "even"
Have fun!
'''
def odd_or_even(arr):
    arrsum = sum(arr)
    if arrsum % 2 == 0:
        return "even"
    else:
        return "odd"


print(odd_or_even([0, 1, 2])) #print "odd"
print(odd_or_even([0, 1, 3])) #print "even"
print(odd_or_even([1023, 1, 2])) #print "even"
print(odd_or_even([0])) #print "even"
print(odd_or_even([0, 1, 4])) #print "odd"
print(odd_or_even([0, -1, -5])) #print "even"

inputlist = [0, 1, 4]
inputlist = []
print(sum(inputlist)) #print 0
inputlistsum = sum(inputlist)
if inputlistsum % 2 == 0:
    print("even") #print even
else:
    print("ddd")

#User solution
def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'