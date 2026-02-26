#https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python
'''
Remove duplicates from list 8 kyu

Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

The order of the sequence has to stay the same.

Examples:

Input -> Output
[1, 1, 2] -> [1, 2]
[1, 2, 1, 1, 3, 2] -> [1, 2, 3]
'''
def distinct(seq):
    return list(dict.fromkeys(seq))


print(distinct([1])) #print [1]
print(distinct([1, 2])) #print [1, 2]
print(distinct([1, 1, 2])) #print [1, 2]
print(distinct([1, 1, 1, 2, 3, 4, 5])) #print [1, 2, 3, 4, 5]
print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7])) #print [1, 2, 3, 4, 5, 6, 7]

#Instructions said The order of the sequence has to stay the same.  The program below doesn't work.
usesetsremoveduplicates = [1, 1, 1, 2, 3, 4, 4, 4, 5]
print(usesetsremoveduplicates) #print [1, 1, 1, 2, 3, 4, 4, 4, 5]
print(set(usesetsremoveduplicates)) #print {1, 2, 3, 4, 5}
print(list(set(usesetsremoveduplicates))) #print [1, 2, 3, 4, 5].  Convert set to list.

#Google AI first search result use dict.fromkeys
def distinct(seq):
    return list(dict.fromkeys(seq))

#User solution
def distinct(seq):
    return sorted(set(seq), key=seq.index)
