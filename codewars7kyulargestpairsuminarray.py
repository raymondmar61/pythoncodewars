#https://www.codewars.com/kata/556196a6091a7e7f58000018/train/python
'''
Largest pair sum in array 7 kyu

Given a sequence of numbers, find the largest pair sum in the sequence.

For example

[10, 14, 2, 23, 19] -->  42 (= 23 + 19)
[99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
Input sequence contains minimum two elements and every element is an integer.
'''
def largest_pair_sum(numbers):
    numbers.sort()
    return numbers[-1] + numbers[-2]


print(largest_pair_sum([10, 14, 2, 23, 19])) #print 42
print(largest_pair_sum([-100, -29, -24, -19, 19])) #print 0
print(largest_pair_sum([1, 2, 3, 4, 6, -1, 2])) #print 10
print(largest_pair_sum([-10, -8, -16, -18, -19])) #print -18

inputnumbers = [10, 14, 2, 23, 19]
inputnumbers = [99, 2, 2, 23, 19]
inputnumbers.sort()
print(inputnumbers[-1] + inputnumbers[-2]) #print 122
