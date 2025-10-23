#https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python
'''
Two to One 7kyu

Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string (alphabetical ascending), the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''
def longest(a1, a2):
    combinea1a2 = a1 + a2
    removeduplicates = list(set([*combinea1a2]))
    removeduplicates.sort()
    return "".join(removeduplicates)


teststringa = "xyaabbbccccdefww"
teststringb = "xxxxyyyyabklmopq"
print(longest(teststringa, teststringb)) #print abcdefklmopqwxy
teststringa = "abcdefghijklmnopqrstuvwxyz"
teststringb = "abcdefghijklmnopqrstuvwxyz"
print(longest(teststringa, teststringb)) #print abcdefghijklmnopqrstuvwxyz


teststringa = "xyaabbbccccdefww"
teststringb = "xxxxyyyyabklmopq"
teststring = teststringa + teststringb
print([*teststring]) #print ['x', 'y', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'e', 'f', 'w', 'w', 'x', 'x', 'x', 'x', 'y', 'y', 'y', 'y', 'a', 'b', 'k', 'l', 'm', 'o', 'p', 'q']
removeduplicates = list(set([*teststring]))
removeduplicates.sort()
print(removeduplicates) #print ['a', 'b', 'c', 'd', 'e', 'f', 'k', 'l', 'm', 'o', 'p', 'q', 'w', 'x', 'y']
print("".join(removeduplicates)) #print abcdefklmopqwxy

teststringa = "abcdefghijklmnopqrstuvwxyz"
teststringb = "abcdefghijklmnopqrstuvwxyz"
teststring = teststringa + teststringb
print([*teststring]) #print ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
removeduplicates = list(set([*teststring]))
removeduplicates.sort()
print(removeduplicates) #print ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("".join(removeduplicates)) #print abcdefghijklmnopqrstuvwxyz
