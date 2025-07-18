#https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python
'''
Take a Number And Sum Its Digits Raised To The Consecutive Powers And .... Eureka!! 6kyu

Description:
The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata.  What's the use of saying "Eureka"?  Because this sum gives the same number:  89 = 8^1 + 9^2 or 8 + 81

The next number in having this property is 135:  See this property again: 135 = 1^1 + 3^2 + 5^3 or 1 + 9 + 125

Task

We need a function to collect these numbers, that may receive two integers a, b that defines the range [a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Examples

Let's see some cases (input -> output):

1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

If there are no numbers of this kind in the range [a,b] the function should output an empty list.

90, 100 --> []

Enjoy it!!
'''
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    outputlist = []
    rangelist = list(range(a, b + 1))
    for n in rangelist:
        numberstring = str(n)
        numberstringlength = len(numberstring)
        stringeachnumber = [*str(n)]
        eurekasum = 0
        exponent = 1
        for x in stringeachnumber:
            eurekasum += int(x)**exponent
            exponent += 1
        if eurekasum == n:
            outputlist.append(n)
    return outputlist

#RM:  confirmed sum_dig_pow(a,b) function works.

outputlist = []
a = 1
b = 10
print(list(range(a, b + 1))) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rangelist = list(range(a, b + 1))
for n in rangelist:
    numberstring = str(n)
    numberstringlength = len(numberstring)
    stringeachnumber = [*str(n)]
    print(stringeachnumber) #print ['1']
    eurekasum = 0
    exponent = 1
    for x in stringeachnumber:
        print("n=", n) #print n= 1
        print("x=", x) #print x= 1
        eurekasum += int(x)**exponent
        print("eurekasum=", eurekasum) #print eurekasum= 1
        exponent += 1
    if eurekasum == n:
        outputlist.append(n)
print(outputlist) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

#Enumerate assign a number with an item in a list.  Index numbers for each list entry.  Enumerate supplies a corresponding index to each element in the list that you pass it.  Each time you go through the loop, index will be one greater, and item will be the next item in the sequence.  It's very similar to using a normal for loop with a list, except this gives us an easy way to count how many items we've seen so far.
print(enumerate(rangelist)) #print <enumerate object at 0x70ca6698b900>
print(list(enumerate(rangelist))) #print [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
seasons = ["fall", "winter", "spring", "summer"]
print(list(enumerate(seasons))) #print [(0, 'fall'), (1, 'winter'), (2, 'spring'), (3, 'summer')]
for each in list(enumerate(seasons)):
    print(each)
    print(each[0])
    print(each[0] + 1)
    print(each[1])
    '''
    (0, 'fall')
    0
    1
    fall
    (1, 'winter')
    1
    2
    winter
    ...
    '''
for index, value in list(enumerate(seasons)):
    print(index, value)
    '''
    0 fall
    1 winter
    2 spring
    3 summer
    '''
