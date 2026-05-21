#https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce/train/python
'''
No oddities here 7 kyu

Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given.
'''
def no_odds(values):
    return [eachvalues for eachvalues in values if eachvalues % 2 == 0]


print(no_odds([0, 1])) #print [0]
print(no_odds([0, 1, 2, 3])) #print [0, 2]
print(no_odds([1, 3, 5, 7, 9])) #print []
print(no_odds([0, 2, 4, 6, 8, 10])) #print [0, 2, 4, 6, 8, 10]
print(no_odds([-1, -3, -5, -7, -9])) #print []
print(no_odds([2, 4, 8, 6, 0])) #print [2, 4, 8, 6, 0]
print(no_odds([])) #print []


integersarray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evenintegers = [eachintegersarray for eachintegersarray in integersarray if eachintegersarray % 2 == 0]
print(evenintegers) #print [2, 4, 6, 8]

decimalsletters = [1.5, 2.3, 4.4, 5.4, "n", 1.5, 5.1, "a"]
extractnumbers = [decimals for decimals in decimalsletters if not isinstance(decimals, str)]
print(extractnumbers) #print [1.5, 2.3, 4.4, 5.4, 1.5, 5.1]
