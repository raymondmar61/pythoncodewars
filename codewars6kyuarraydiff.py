#https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
'''
Array.diff 6kyu

Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). The order of elements in the first list should be preserved in the result.

Examples
If a = [1, 2] and b = [1], the result should be [2].

If a = [1, 2, 2, 2, 3] and b = [2], the result should be [1, 3].
'''
def array_diff(a, b):
    answerlist = []
    for x in a:
        if x not in b:
            answerlist.append(x)
    return answerlist


a = [1, 2]
b = [1]
a = set(a)
b = set(b)
print(a.symmetric_difference(b)) #print {2}
a = [1, 2, 2, 2, 3]
b = [2]
a = set(a)
b = set(b)
print(a.symmetric_difference(b)) #print {1, 3}
a = [1, 2, 2]
b = [1]
a = set(a)
b = set(b)
difference = list(set(a) - set(b))
print(difference) #print [2]

#https://stackoverflow.com/questions/4211209/remove-all-the-elements-that-occur-in-one-list-from-another
a = []
b = [1, 2]
answerlist = []
for x in a:
    if x not in b:
        answerlist.append(x)
print(answerlist) #print [].  RM:  correct answer

print(array_diff([1, 2], [1])) #print [2]
print(array_diff([1, 2, 2, 2, 3], [2])) #print [1, 3]
