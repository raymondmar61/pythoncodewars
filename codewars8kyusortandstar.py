#https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python
'''
Sort and Star 8kyu

You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.

RM:  Sort the list alphabetically case sensitive.
'''
def two_sort(array):
    array.sort()
    return ("***".join(array[0]))


print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"])) #print b***i***t***c***o***i***n
print(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"])) #print a***r***e
print(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"])) #print a***b***o***u***t
print(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"])) #print c***o***d***e
print(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"])) #print L***e***t***s

testlist = ["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones", "Lets"]
testlist.sort()
print(testlist) #print ['Lets', 'are', 'basic', 'cases', 'easier', 'ones', 'out', 'out', 'random', 'test', 'than', 'turns', 'writing']
print(testlist[0]) #print Lets
print(type(testlist[0])) #print <class 'str'>
print("***".join(testlist[0])) #print L***e***t***s
