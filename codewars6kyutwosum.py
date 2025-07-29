#https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
'''
Two Sum 6kyu

Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indexes of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: https://leetcode.com/problems/two-sum/

two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)
two_sum([3, 2, 4], 6) # returns (1, 2) or (2, 1)
'''
import itertools
def two_sum(numbers, target):
    numberslist = numbers
    numbersenumerate = list(enumerate(numberslist))
    numberslistcombinationindex = list(range(0, len(numberslist)))
    numberslistcombinationindexlist = list(itertools.combinations(numberslistcombinationindex, 2))
    for x in numberslistcombinationindexlist:
        if numberslist[x[0]] + numberslist[x[1]] == target:
            return x
            break


print(two_sum([1, 2, 3], 4)) #print (0, 2)
print(two_sum([3, 2, 4], 6)) #print (1, 2)
print(two_sum([1234, 5678, 9012], 14690)) #print (1, 2)
print(two_sum([2, 2, 3], 4)) #print (0, 1)
print(two_sum([2, 7, 11, 15], 9)) #print (0, 1)
print(two_sum([3, 3], 6)) #print (0, 1)


numberslist = [1, 2, 3]
print(itertools.combinations(numberslist, 2)) #print <itertools.combinations object at 0x733aa097dd50>
print(list(itertools.combinations(numberslist, 2))) #print [(1, 2), (1, 3), (2, 3)]
print("\n")

numberslist = [1234, 5678, 9012]
print(list(enumerate(numberslist))) #print [(0, 1234), (1, 5678), (2, 9012)]
numberslistenumerate = list(enumerate(numberslist))
for index, value in numberslistenumerate:
    print(index, value)
    '''
    0 1234
    1 5678
    2 9012
    '''
numberslistcombinationindex = list(range(0, len(numberslist)))
print(numberslistcombinationindex) #print [0, 1, 2]
print(list(itertools.combinations(numberslistcombinationindex, 2))) #print [(0, 1), (0, 2), (1, 2)]
numberslistcombinationindexlist = list(itertools.combinations(numberslistcombinationindex, 2))
for x in numberslistcombinationindexlist:
    print(x)
    print(x[0])
    print(x[1])
    '''
    (0, 1)
    0
    1
    '''
for x in numberslistcombinationindexlist:
    print(numberslist[x[0]]) #print 5678
    print(numberslist[x[1]]) #print 9012
    print("sum", numberslist[x[0]] + numberslist[x[1]]) #print sum 14690
    if numberslist[x[0]] + numberslist[x[1]] == 14690:
        print(x) #print (1, 2)
        break
