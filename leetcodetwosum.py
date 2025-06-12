#https://leetcode.com/problems/two-sum/description/
'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

*2 <= nums.length <= 104
*-109 <= nums[i] <= 109
*-109 <= target <= 109
*Only one valid answer exists.
'''
import itertools
def twosums(numberlist, targetnumber):
    outputlist = []
    combinationlist = itertools.combinations(numberlist, 2)
    for eachcombinationlist in combinationlist:
        if sum(eachcombinationlist) == targetnumber:
            index1 = numberlist.index(eachcombinationlist[0], 0)
            index2 = numberlist.index(eachcombinationlist[1], index1 + 1)
            outputlist.append(index1)
            outputlist.append(index2)
            # outputlist.append(numberlist.index(eachcombinationlist[0])), outputlist.append(numberlist.index(eachcombinationlist[1], numberlist.index(eachcombinationlist[0]) + 1))
    print(outputlist)


twosums([2, 7, 11, 15], 9) #return [0, 1]
twosums([3, 2, 4], 6) #return [1, 2]
twosums([3, 3], 6) #return [0, 1]

numberlist = [2, 7, 11, 15]
targetnumber = 9
outputlist = []
print(list(itertools.combinations(numberlist, 2))) #print [(2, 7), (2, 11), (2, 15), (7, 11), (7, 15), (11, 15)]
combinationlist = itertools.combinations(numberlist, 2)
for eachcombinationlist in combinationlist:
    print(sum(eachcombinationlist)) #print 9
    if sum(eachcombinationlist) == targetnumber:
        print(eachcombinationlist[0], eachcombinationlist[1]) #print 2 7
        print(numberlist.index(eachcombinationlist[0]), numberlist.index(eachcombinationlist[1]))
        outputlist.append(numberlist.index(eachcombinationlist[0])), outputlist.append(numberlist.index(eachcombinationlist[1])) #print 0 1
        break
print(outputlist) #print [0, 1]
