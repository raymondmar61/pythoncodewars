#https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python
'''
Remove the minimum 7 kyu

The museum of incredibly dull things

The museum of incredibly dull things wants to get rid of some exhibits. Miriam, the interior architect, comes up with a plan to remove the most boring exhibits. She gives them a rating, and then removes the one with the lowest rating.

However, just as she finished rating all exhibits, she's off to an important fair, so she asks you to write a program that tells her the ratings of the exhibits after removing the lowest one. Fair enough.

Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

Examples
* Input: [1,2,3,4,5], output = [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]
'''

#Google AI:  To solve the Codewars 7 kyu "Remove the minimum" kata, create a copy of the input list, find the index or value of the smallest element, remove only the first occurrence of that minimum value, preserve the original order of the remaining elements, and return an empty list if the input is empty.
def remove_smallest(numbers):
    copynumbers = numbers.copy()
    if copynumbers:
        lowestrating = min(copynumbers)
        copynumbers.remove(lowestrating)
        return copynumbers
    else:
        return []


print(remove_smallest([1, 2, 3, 4, 5])) #print [2, 3, 4, 5]
print(remove_smallest([5, 3, 2, 1, 4])) #print [5, 3, 2, 4]
print(remove_smallest([1, 2, 3, 1, 1])) #print [2, 3, 1, 1]
print(remove_smallest([])) #print []
print(remove_smallest([2, 2, 1, 2, 1])) #print []

ratinglist = [5, 3, 2, 1, 4]
print(min(ratinglist))
ratinglist = [2, 2, 1, 2, 1]
print(min(ratinglist))
lowestrating = min(ratinglist)
ratinglist.remove(lowestrating)
print(ratinglist)

#User solution
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a
