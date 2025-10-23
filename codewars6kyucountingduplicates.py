#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
'''
Counting Duplicates

Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
'''
from collections import Counter
def duplicate_count(text):
    textinputlowercase = text.lower()
    countsplittextinput = Counter(textinputlowercase).most_common()
    countduplicates = 0
    for eachstring, counteachstring in countsplittextinput:
        if counteachstring > 1:
            countduplicates += 1
    return countduplicates


print(duplicate_count("abcde")) #print 0
print(duplicate_count("aabbcde")) #print 2
print(duplicate_count("aabBcde")) #print 2
print(duplicate_count("indivisibility")) #print 1
print(duplicate_count("Indivisibilities")) #print 2
print(duplicate_count("aA11")) #print 2
print(duplicate_count("ABBA")) #print 2
