#https://www.codewars.com/kata/54d81488b981293527000c8f/train/python
'''
Sum of Pairs 5 kyu
Sum of Pairs
Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

If there are two or more pairs with the required sum, the pair whose second element has the smallest index is the solution.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * the correct answer is the pair whose second value has the smallest index
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined/Nothing (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * the correct answer is the pair whose second value has the smallest index
== [3, 7]

Negative numbers and duplicate numbers can and will appear.

NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.
'''
from operator import itemgetter
from itertools import combinations
def sum_pairs(ints, s):
    integerslistlength = len(ints)
    integerslistindexnumbers = [n for n in range(0, integerslistlength)]
    integerslistindexnumberscombinations = list(combinations(integerslistindexnumbers, 2))
    integerslistindexnumberscombinations.sort(key=itemgetter(1))
    minimumsecondindex = 0
    answerpair = []
    for x in integerslistindexnumberscombinations:
        firstindex = x[0]
        secondindex = x[1]
        xsum = ints[firstindex] + ints[secondindex]
        if xsum == s:
            answerpair.append([firstindex, secondindex])
            break
    if answerpair == []:
        return None
    else:
        return [ints[answerpair[0][0]], ints[answerpair[0][1]]]


print(sum_pairs([11, 3, 7, 5], 10)) #print [3 ,7]
print(sum_pairs([4, 3, 2, 3, 4], 6)) #print [4, 2]
print(sum_pairs([0, 0, -2, 3], 2)) #print None
print(sum_pairs([10, 5, 2, 3, 7, 5], 10)) #print [3 ,7]
print(sum_pairs([1, 4, 8, 7, 3, 15], 8)) #print [1, 7]
print(sum_pairs([1, -2, 3, 0, -6, 1], -6)) #print [0, -6]
print(sum_pairs([20, -13, 40], -7)) #print None
print(sum_pairs([1, 2, 3, 4, 1, 0], 2)) #print [1, 1]
print(sum_pairs([10, 5, 2, 3, 7, 5], 10)) #print [3, 7]
print(sum_pairs([4, -2, 3, 3, 4], 8)) #print [4, 4]
print(sum_pairs([0, 2, 0], 0)) #print [0, 0]
print(sum_pairs([5, 9, 13, -3], 10)) #print [13, -3]
l9 = [1] * 10000000
l9[len(l9) // 2 - 1] = 6
l9[len(l9) // 2] = 7
l9[len(l9) - 2] = 8
l9[len(l9) - 1] = -3
l9[0] = 13
l9[1] = 3
#print(sum_pairs(l9, 13)) #print [6, 7] #RM:  I don't understand the l9.  The first sum_pairs function timed out running print(sum_pairs(l9, 13)).


integerslist = [0, 0, -2, 3]
singlesumvalue = 2
integerslist = [4, -2, 3, 3, 4]
singlesumvalue = 8
integerslist = [10, 5, 2, 3, 7, 5]
singlesumvalue = 10
integerslist = [4, 3, 2, 3, 4]
singlesumvalue = 6
print(len(integerslist))
integerslistlength = len(integerslist)
integerslistindexnumbers = [n for n in range(0, integerslistlength)]
print(integerslistindexnumbers)
print(list(combinations(integerslistindexnumbers, 2)))
integerslistindexnumberscombinations = list(combinations(integerslistindexnumbers, 2))
integerslistindexnumberscombinations.sort(key=itemgetter(1))
minimumsecondindex = 0
answerpair = []
for x in integerslistindexnumberscombinations:
    print(x)
    print(x[0], x[1])
    firstindex = x[0]
    secondindex = x[1]
    print(integerslist[firstindex], integerslist[secondindex])
    xsum = integerslist[firstindex] + integerslist[secondindex]
    print(xsum)
    if xsum == singlesumvalue:
        print("\t love")
        print("\t", firstindex, secondindex)
        answerpair.append([firstindex, secondindex])
        print(answerpair)
        answerpair.sort(key=itemgetter(1))
        print(answerpair)
        print(integerslist[answerpair[0][0]], integerslist[answerpair[0][1]])
        break
print(answerpair)
print(integerslist[answerpair[0][0]], integerslist[answerpair[0][1]])
'''
[0, 1, 2, 3, 4]
[(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
(0, 1)
0 1
4 3
7
(0, 2)
0 2
4 2
6
     love
     0 2
[[0, 2]]
[[0, 2]]
4 2
[[0, 2]]
4 2
'''

sortsecondindex = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
print(sortsecondindex) #print [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
sortsecondindex.sort(key=itemgetter(1))
print(sortsecondindex) #print [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3), (0, 4), (1, 4), (2, 4), (3, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)]


#Google AI
#A nested loop causes a "Time Limit Exceeded" error.  Use a hash map which is a dictionary in Python to iterate through the list exactly once.  Calculate the difference between the target sum and the current number.  If this difference exists in your hash map, you've found your pair.  If it doesn't, add the current number to the hash map and move to the next.
#The function below automatically guarantees the pair with the lowest index for the second number is returned because we check for matches before adding to the cache.
def sum_pairs(ints, s):
    hashmapdictionary = {}
    for num in ints:
        print(f"num {num}")
        difference = s - num
        print(f"difference {difference} = {s} - {num}")
        print(f"hashmapdictionary1 {hashmapdictionary}")
        if difference in hashmapdictionary:
            return [difference, num]
        hashmapdictionary[num] = True
        print(f"hashmapdictionary2 {hashmapdictionary}")
    return None


print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
'''
num 10
difference 0 = 10 - 10
hashmapdictionary1 {}
hashmapdictionary2 {10: True}
num 5
difference 5 = 10 - 5
hashmapdictionary1 {10: True}
hashmapdictionary2 {10: True, 5: True}
num 2
difference 8 = 10 - 2
hashmapdictionary1 {10: True, 5: True}
hashmapdictionary2 {10: True, 5: True, 2: True}
num 3
difference 7 = 10 - 3
hashmapdictionary1 {10: True, 5: True, 2: True}
hashmapdictionary2 {10: True, 5: True, 2: True, 3: True}
num 7
difference 3 = 10 - 7
hashmapdictionary1 {10: True, 5: True, 2: True, 3: True}
[3, 7]
'''

#https://zhuangyan.gitbooks.io/codewars/content/5-kyu/sum-of-pairs.html
def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

def sum_pairs(nums, sum_value):
    seen = set()
    for num in nums:
        diff = sum_value - num
        if diff in seen:
            return [diff, num]
        seen.add(num)
