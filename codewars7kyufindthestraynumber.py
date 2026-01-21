#https://www.codewars.com/kata/57f609022f4d534f05000024/train/python
'''
Find the stray number 7kyu

You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
'''
from collections import Counter
def stray(arr):
    countnumbers = Counter(arr)
    return countnumbers.most_common()[-1][0]


print(stray([1, 1, 2])) #print 2
print(stray([17, 17, 3, 17, 17, 17, 17])) #print 3
print(stray([1, 1, 1, 1, 1, 1, 2])) #print 2
print(stray([2, 3, 2, 2, 2])) #print 3
print(stray([3, 2, 2, 2, 2])) #print 3

integerslist = [17, 17, 3, 17, 17, 17, 17]
print(integerslist) #print [17, 17, 3, 17, 17, 17, 17]
countnumbers = Counter(integerslist)
print(countnumbers) #print Counter({17: 6, 3: 1})
print(type(countnumbers)) #print <class 'collections.Counter'>
print(countnumbers.most_common()[-1]) #print (3, 1)
print(countnumbers.most_common()[-1][0]) #print 3

#User submission
def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x

def stray(arr):
    return min(arr, key=arr.count)
