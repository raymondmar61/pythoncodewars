#https://www.codewars.com/kata/5a805d8cafa10f8b930005ba/train/python
'''
Find Nearest square number 8 kyu

Your task is to find the nearest square number of a positive integer n. In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

For example, if n = 111, then the nearest square number equals 121, since 111 is closer to 121, the square of 11, than 100, the square of 10.

If n is already a perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.

Good luck :)
'''
from math import sqrt
def nearest_sq(n):
    initialn = n #create variable initialn for the input n variable
    root = sqrt(n)
    if root % 1 == 0: #If n is a perfect square root, then return n
        return n
    else:
        solutionlist = []
        counterpositive = 1
        #Find nearest square number adding 1 to n
        while True:
            root = sqrt(n)
            if root % 1 == 0:
                solutionlist.append((counterpositive, n))
                break
            n += 1
            counterpositive += 1
        n = initialn
        counternegative = 1
        #Find nearest square number subtracting 1 to n
        while True:
            root = sqrt(n)
            if root % 1 == 0:
                solutionlist.append((counternegative, n))
                break
            n -= 1
            counternegative += 1
    return (min(solutionlist)[1])


print(nearest_sq(1)) #print 1
print(nearest_sq(2)) #print 1
print(nearest_sq(10)) #print 9
print(nearest_sq(111)) #print 121
print(nearest_sq(9999)) #print 10000

solutionlist = []
n = 111
print(n) #print 111
counterpositive = 1
while True:
    root = sqrt(n)
    print(root) #print 10.535653752852738\n . . .
    if root % 1 == 0:
        break
    n += 1
    counterpositive += 1
print(counterpositive, n) #print 11 121
solutionlist.append((counterpositive, n))

n = 111
print(n) #print 111
counternegative = 1
while True:
    root = sqrt(n) #print 10.535653752852738\n . . .
    print(root)
    if root % 1 == 0:
        break
    n -= 1
    counternegative += 1
print(counternegative, n) #print 12 100
solutionlist.append((counternegative, n))
print(solutionlist) #print [(11, 121), (12, 100)]
print(min(solutionlist)) #print (11, 121)
print(min(solutionlist)[1]) #print 121

#User solution
def nearest_sq(n):
    return round(n ** 0.5) ** 2
#math.sqrt is much slower than **
'''
For those who are wondering why this works, here's the proof:

Suppose the integer part of sqrt(n) is a and we can have the expression of n as n = a ** 2 + b, where b is also an integer. We want to find the critical value of b, which I will call it k, such that if b < k, the nearest square number of n is a ** 2 and if b >= k, the nearest square number of n is (a + 1) ** 2.

To find k, we first calculate the difference between a ** 2 and (a + 1) ** 2, which is 2a + 1. The half of it is a + 1/2, which implies k = a + 1.

Now, because a ** 2 + a + 1/4 = (a + 1/2) ** 2, one can deduce that sqrt(a ** 2 + a) < sqrt(a ** 2 + a + 1/4) = (a + 1/2) <= sqrt(a ** 2 + a + 1).

That is to say, if the sqrt of a number n is a + a floating point value >= 0.5, then b >= k + 1; if the floating point value is < 0.5, otherwise.

Thus, round(n) would definitely yield a or a + 1, whichever has its square value nearest to n.
'''