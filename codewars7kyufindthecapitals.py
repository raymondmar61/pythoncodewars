#https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python
'''
Find the capitals 7 kyu

Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.

Example (Input --> Output)
"CodEWaRs" --> [0,3,4,6]
'''
def capitals(word):
    return [n for n in range(0, len(word)) if word[n].isupper()]


print(capitals("CodEWaRs")) #print [0, 3, 4, 6]


asciiword = "CodEWaRs"
for n in range(0, len(asciiword)):
    print(asciiword[n])
    print(asciiword[n].isupper())
    '''
    C
    True
    o
    False
    d
    False
    E
    True
    W
    True
    a
    False
    R
    True
    s
    False
    '''

listcomprehension = [n for n in range(0, len(asciiword)) if asciiword[n].isupper()]
print(listcomprehension) #print [0, 3, 4, 6]

#User solution
def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]
