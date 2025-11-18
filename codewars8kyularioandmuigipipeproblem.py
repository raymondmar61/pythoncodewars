#https://www.codewars.com/kata/56b29582461215098d00000f/train/python
'''
Lario and Muigi Pipe Problem 8kyu

Issue
Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.

The pipes connecting your level's stages together need to be fixed before you receive any more complaints.

The pipes are correct when each pipe after the first is 1 more than the previous one.

Task
Given a list of unique numbers sorted in ascending order, return a new list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included).

Example
Input:  1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8
'''
def pipe_fix(nums):
    return [n for n in range(min(nums), max(nums) + 1)]


print(pipe_fix([1, 2, 3, 5, 6, 8, 9])) #print [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(pipe_fix([1, 2, 3, 12])) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(pipe_fix([6, 9])) #print [6, 7, 8, 9]
print(pipe_fix([-1, 4])) #print [-1, 0, 1, 2, 3, 4]
print(pipe_fix([1, 2, 3])) #print [1, 2, 3]

listuniqenumbers = [1, 3, 5, 6, 7, 8]
listuniqenumbers.sort()
startinglevel = listuniqenumbers[0]
endinglevel = listuniqenumbers[-1]
print(startinglevel, endinglevel) #print 1 8
print([n for n in range(startinglevel, endinglevel + 1)]) #print [1, 2, 3, 4, 5, 6, 7, 8]


print(min(listuniqenumbers), max(listuniqenumbers)) #print 1 8
print([n for n in range(min(listuniqenumbers), max(listuniqenumbers) + 1)]) #print [1, 2, 3, 4, 5, 6, 7, 8]
