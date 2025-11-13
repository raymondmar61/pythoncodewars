#https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python
'''
Count the divisors of a number 7kyu

Count the number of divisors of a positive integer n.

Random tests go up to n = 500000, but fixed tests go higher.

Examples (input --> output)
4 --> 3 // we have 3 divisors - 1, 2 and 4
5 --> 2 // we have 2 divisors - 1 and 5
12 --> 6 // we have 6 divisors - 1, 2, 3, 4, 6 and 12
30 --> 8 // we have 8 divisors - 1, 2, 3, 5, 6, 10, 15 and 30

Note you should only return a number, the count of divisors. The numbers between parentheses are shown only for you to see which numbers are counted in each case.
'''
def divisors(n):
    count = 1
    for divisor in range(1, n):
        if n % divisor == 0:
            count += 1
    return count


print(divisors(1)) #print 1
print(divisors(4)) #print 3
print(divisors(5)) #print 2
print(divisors(12)) #print 6
print(divisors(30)) #print 8
print(divisors(4096)) #print 13

dividend = 12
count = 1 #count starts at 1 because the dividend equals the divisor divided by the divisor is a divisor.  12 % 12 == 0 count +1.
for divisor in range(1, dividend):
    if dividend % divisor == 0:
        print("dividend", divisor)
        '''
        dividend 1
        dividend 2
        dividend 3
        dividend 4
        dividend 6
        '''
        count += 1
print(count) #print 6

#User submitted
def divisors2(n):
    return sum([n % x == 0 for x in range(1, n + 1)])