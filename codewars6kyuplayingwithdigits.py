#https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
'''
Playing with digits 6 kyu

Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴ = 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that: (a^p + b^p+1 + c^p+2 + d^p+3 + . . . = n*k)

If it is the case we will return k, if not return -1.

Note: n and p will always be strictly positive integers.

n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1

n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k

n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2

n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
'''
def dig_pow(n, p):
    numberlist = list(map(int, str(n)))
    numberlistsum = 0
    for eachnumberlist in numberlist:
        numberlistsum += (eachnumberlist**p)
        p += 1
    k = 1
    while True:
        if numberlistsum == n * k:
            return k
            break
        elif numberlistsum < n * k:
            return -1
            break
        k += 1


print(dig_pow(89, 1)) #print 1
print(dig_pow(92, 1)) #print -1
print(dig_pow(695, 2)) #print 2
print(dig_pow(46288, 3)) #print 51
print(dig_pow(41, 5)) #print 25
print(dig_pow(114, 3)) #print 9
print(dig_pow(8, 3)) #print 64

number = 46288
power = 3
numberlist = list(map(int, str(number)))
print(numberlist) #print [4, 6, 2, 8, 8]
numberlistsum = 0
for eachnumberlist in numberlist:
    print(f"{eachnumberlist} ^ {power} = {eachnumberlist**power}")
    '''
    4 ^ 3 = 64
    6 ^ 4 = 1296
    2 ^ 5 = 32
    8 ^ 6 = 262144
    8 ^ 7 = 2097152
    '''
    numberlistsum += (eachnumberlist**power)
    power += 1
print(numberlistsum) #print 2360688
findk = 1
while True:
    if numberlistsum == number * findk:
        print(findk) #print 51
        break
    elif numberlistsum < number * findk:
        print(-1)
        break
    findk += 1

#User submission
def dig_pow(n, p):
    s = 0
    for i, c in enumerate(str(n)):
        s += pow(int(c), p + i)
        return s / n if s % n == 0 else -1
