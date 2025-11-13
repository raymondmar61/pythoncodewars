#https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
'''
Find the unique number 6kyu

There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique
'''
import numpy as np
def find_uniq(arr):
    countitemsunique = np.array(arr)
    unique, counts = np.unique(countitemsunique, return_counts=True)
    dictionaryresults = dict(zip(unique, counts)) #print {0: 4, 10: 1, 20: 7, 30: 3}
    findnumberonevalue = [key for key, value in dictionaryresults.items() if value == 1]
    return findnumberonevalue[0]


print(find_uniq([1, 1, 1, 2, 1, 1])) #print 2
print(find_uniq([0, 0, 0.55, 0, 0])) #print 0.55


countitemsunique = np.array([10, 20, 20, 20, 20, 0, 20, 30, 30, 30, 0, 0, 20, 20, 0])
unique, counts = np.unique(countitemsunique, return_counts=True)
print(dict(zip(unique, counts))) #print {0: 4, 10: 1, 20: 7, 30: 3}
love = dict(zip(unique, counts))
#Is there a way to find a key in a dictionary with only knowing the value?  You will need to iterate.  To loop even though it's not efficient.
#https://www.reddit.com/r/learnpython/comments/yfmnhm/is_there_a_way_to_find_a_key_in_a_dictionary_with/
findnumberonevalue = [key for key, value in love.items() if value == 1]
print(findnumberonevalue) #print [10]

#User submission
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


from collections import Counter

def find_uniq(a):
    return Counter(a).most_common()[-1][0]
