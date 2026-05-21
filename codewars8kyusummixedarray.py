#https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python
'''
Sum Mixed Array 8 kyu

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.
'''
def sum_mix(arr):
    trueintegerslist = list(map(int, arr))
    return sum(trueintegerslist)


print(sum_mix([9, 3, '7', '3'])) #print 22
print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7])) #print 42
print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0'])) #print 41
print(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3'])) #print 45
print(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7])) #print 61

integerslist = [1, 2, "3", 4, "5"]
trueintegerslist = list(map(int, integerslist))
print((sum(trueintegerslist))) #print 15
