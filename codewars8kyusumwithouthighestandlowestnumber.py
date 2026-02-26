#https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
'''
Sum without highest and lowest number 8 kyu

Task
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element (by value, not by index!).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

Example
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6

Input validation
If an empty value (null, None, Nothing, nil etc.) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.
'''
def sum_array(arr):
    if not arr:
        return 0
    elif len(arr) == 1 or len(arr) == 2:
        return 0
    else:
        arr.sort()
        return sum(arr[1:-1])


print(sum_array(None)) #print 0
print(sum_array([])) #print 0
print(sum_array([3])) #print 0
print(sum_array([-3])) #print 0
print(sum_array([3, 5])) #print 0
print(sum_array([-3, -5])) #print 0
print(sum_array([6, 2, 1, 8, 10])) #print 16
print(sum_array([6, 0, 1, 10, 10])) #print 17
print(sum_array([-6, -20, -1, -10, -12])) #print -28
print(sum_array([-6, 20, -1, 10, -12])) #print 3
print(sum_array([1, 2, 3])) #print 2

print(sum([1, 2, 3, 4])) #print 10
testlist = [-6, 20, -1, 10, -12]
testlist.sort()
print(testlist) #print [-12, -6, -1, 10, 20]
addtestlist = testlist[1:-1]
print(addtestlist) #print [-6, -1, 10]
print(sum(addtestlist)) #print 3
oneelement = [3]
print(oneelement[1:-1]) #print []
