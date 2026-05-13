#https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python
'''
Flatten and sort an array 7 kyu

Challenge:

Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.

Example:

Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].
'''
def flatten_and_sort(array):
    flatlistnestedlistcomprehension = [item for sublist in array for item in sublist]
    flatlistnestedlistcomprehension.sort()
    return flatlistnestedlistcomprehension


print(flatten_and_sort([])) #print []
print(flatten_and_sort([[], []])) #print []
print(flatten_and_sort([[], [1]])) #print [1]
print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]])) #print [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]])) #print [1, 2, 3, 4, 5, 6, 100]
print(flatten_and_sort([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]])) #print [1, 2, 3, 4, 5, 6, 7, 8, 9]

givenlist = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
basicforloops = []
for eachgivenlist in givenlist:
    for eachitem in eachgivenlist:
        basicforloops.append(eachitem)
print(basicforloops) #print [3, 2, 1, 4, 6, 5, 9, 7, 8]
flatlistnestedlistcomprehension = [item for sublist in givenlist for item in sublist]
print(flatlistnestedlistcomprehension) #print [3, 2, 1, 4, 6, 5, 9, 7, 8]
flatlistextend = []
for eachgivenlist in givenlist:
    flatlistextend.extend(eachgivenlist)
print(flatlistextend) #print [3, 2, 1, 4, 6, 5, 9, 7, 8]
flatlistsum = sum(givenlist, [])
print(flatlistsum) #print [3, 2, 1, 4, 6, 5, 9, 7, 8]
import itertools
flatlistitertoolschain = list(itertools.chain.from_iterable(givenlist))
print(flatlistitertoolschain) #print [3, 2, 1, 4, 6, 5, 9, 7, 8]
flatlistitertoolschain2 = list(itertools.chain(*givenlist))
print(flatlistitertoolschain2) #print [3, 2, 1, 4, 6, 5, 9, 7, 8]
import numpy as np
flatlistnumpy = np.concatenate(givenlist).tolist()
print(flatlistnumpy) #print [3.0, 2.0, 1.0, 4.0, 6.0, 5.0, 9.0, 7.0, 8.0]
flatlistnumpy2 = np.array(givenlist).flat #VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
print(flatlistnumpy2) #print <numpy.flatiter object at 0x60d7114ea0f0>.  flatlistnumpy2 = np.array(givenlist).flat #VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
flatlistnumpy3 = np.concatenate(givenlist)
print(flatlistnumpy3) #print <numpy.flatiter object at 0x5b77038f58a0>\n [3. 2. 1. 4. 6. 5. 9. 7. 8.]
print(np.concatenate(givenlist)) #print [3. 2. 1. 4. 6. 5. 9. 7. 8.]
