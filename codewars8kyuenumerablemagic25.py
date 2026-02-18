#https://www.codewars.com/kata/545afd0761aa4c3055001386/train/python
'''
Enumerable Magic #25 - Take the First N Elements  8kyu

Create a function that accepts a list/array and a number n, and returns a list/array of the first n elements from the list/array.

If you need help, here's a reference:

https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
'''
def take(arr, n):
    return arr[:n]


print(take([0, 1, 2, 3, 5, 8, 13], 3)) #print [0, 1, 2]


listelements = [0, 1, 2, 3, 5, 8, 13]
returnhowmanyelements = 3
print(listelements[0:returnhowmanyelements])
