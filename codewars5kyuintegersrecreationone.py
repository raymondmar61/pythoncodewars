#https://www.codewars.com/kata/55aa075506463dac6600010d/train/python
'''
Integers: Recreation One 5 kyu

1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246.

Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681.

The sum of these squares is 84100 which is 290 * 290.

Task
Find all integers between m and n (m and n are integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.  RM:  a perfect square.

We will return an array of subarrays or of tuples (in C an array of Pair) or a string.

The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.

Example:
m =  1, n = 250 --> [[1, 1], [42, 2500], [246, 84100]]
m = 42, n = 250 --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see "Sample Tests".

Note
In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.

'''
from math import isqrt, sqrt
def list_squared(m, n):
    solutionlist = []
    while m <= n:
        divisorslist = []
        for divisor in range(1, int(sqrt(m)) + 1):
            if m % divisor == 0:
                #If both divisors are the same or a perfect square, then add once.
                if m // divisor == divisor:
                    divisorslist.append(divisor)
                else:
                    divisorslist.append(divisor)
                    divisorslist.append(m // divisor)
        divisorlistsquared = [eachdivisorlist**2 for eachdivisorlist in divisorslist]
        sumdivisorlistsquared = sum(divisorlistsquared)
        squareroot = isqrt(sumdivisorlistsquared)
        #print(m, sumdivisorlistsquared, squareroot) #print 1 1 1.  42 2500 50.  246 84100 290.
        #Check perfect square root.  If True, then append to solutionlist.
        if squareroot * squareroot == sumdivisorlistsquared:
            solutionlist.append([m, sumdivisorlistsquared])
        m += 1
    return solutionlist


print(list_squared(1, 250)) #print [[1, 1], [42, 2500], [246, 84100]]
print(list_squared(42, 250)) #print [[42, 2500], [246, 84100]]
print(list_squared(250, 500)) #print [[287, 84100]]

from math import sqrt, isqrt
def checkperfectsquare(n):
    if n >= 0:
        squareroot = isqrt(n) #The isqrt() function calculates the integer square root of a given number.
        return (squareroot, squareroot * squareroot == n)


number = 246
divisorlist = []
for divisor in range(1, number + 1):
    if number % divisor == 0:
        divisorlist.append(divisor)
print(divisorlist) #print [1, 2, 3, 6, 41, 82, 123, 246]
divisorlistsquared = [eachdivisorlist**2 for eachdivisorlist in divisorlist]
print(divisorlistsquared) #print [1, 4, 9, 36, 1681, 6724, 15129, 60516]
sumdivisorlistsquared = sum(divisorlistsquared)
print(sumdivisorlistsquared) #print 84100
print(checkperfectsquare(sumdivisorlistsquared)) #print (290, True)
perfectsquaretrueorfalse = checkperfectsquare(sumdivisorlistsquared)
if perfectsquaretrueorfalse[1] == True:
    print([number, sumdivisorlistsquared]) #print [246, 84100]
print(checkperfectsquare(84100)) #print (290, True)

'''
#m =  1, n = 250 --> [[1, 1], [42, 2500], [246, 84100]]
m = 1
n = 250
solutionlist = []
while m <= n:
    divisorlist = []
    for divisor in range(1, m + 1):
        if m % divisor == 0:
            divisorlist.append(divisor)
    divisorlistsquared = [eachdivisorlist**2 for eachdivisorlist in divisorlist]
    sumdivisorlistsquared = sum(divisorlistsquared)
    squareroot = isqrt(sumdivisorlistsquared)
    print(m, sumdivisorlistsquared, squareroot) #print 1 1 1.  42 2500 50.  246 84100 290.
    #Check perfect square root.  If True, then append to solutionlist.
    if squareroot * squareroot == sumdivisorlistsquared:
        solutionlist.append([m, sumdivisorlistsquared])
    m += 1
print(solutionlist) #print [[1, 1], [42, 2500], [246, 84100]]
'''
