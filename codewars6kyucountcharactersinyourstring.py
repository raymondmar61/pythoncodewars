#https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
'''
Count characters in your string 6 kyu

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
'''
def count(s):
    if s:
        stringlikedictionary = dict.fromkeys(s, 0)
        for eachs in s:
            stringlikedictionary[eachs] = stringlikedictionary[eachs] + 1
        return stringlikedictionary
    else:
        return {}


print(count("aba")) #print {'a': 2, 'b': 1}
print(count("")) #print {}
print(count("aa")) #print {'a': 2}
print(count("aabb")) #print {'a': 2, 'b': 2}
print(count("Mississippi")) #print {'M': 1, 'i': 4, 's': 4, 'p': 2}

stringlike = "aba"
stringlikedictionary = dict.fromkeys(stringlike, 0)
print(stringlikedictionary) #print {'a': 0, 'b': 0}
for eachstringlike in stringlike:
    print(eachstringlike)
    print(stringlikedictionary[eachstringlike])
    stringlikedictionary[eachstringlike] = stringlikedictionary[eachstringlike] + 1
    print(stringlikedictionary[eachstringlike])
    '''
    a
    0
    1
    b
    0
    1
    a
    1
    2
    '''
print(stringlikedictionary) #print {'a': 2, 'b': 1}

#User submission
from collections import Counter

def count(string):
    return Counter(string)

def count(string):
    return {i: string.count(i) for i in string}
