#https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python
'''
Product of consecutive Fib numbers 5kyu

The Fibonacci numbers are the numbers in the following integer sequence (Fn): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such that
f(0)=0
f(1)=1
f(2)=1, 1=1+0
f(3)=2, 2=1+1
f(4)=3, 3=2+1
f(5)=5
f(6)=8
f(7)=13
f(8)=21, 21=13+7
f(9)=34, 34=21+13
f(n) = F(n-1)+F(n-2) for n > 1

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying:  F(n)∗F(n+1)=prod

Your function takes an integer (prod) and returns an array/tuple (check the function signature/sample tests for the return type in your language):

if F(n) * F(n+1) = prod:  (F(n), F(n+1), true)

If you do not find two consecutive F(n) verifying F(n) * F(n+1) = prod:  (F(n), F(n+1), false)

where F(n) is the smallest one such as F(n) * F(n+1) > prod.

Examples:
714 ---> (21, 34, true) --> since F(8) = 21, F(9) = 34 and 714 = 21 * 34

800 ---> (34, 55, false) --> since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55.  34*55=1870.  21*34=714.

test.assert_equals(product_fib(4895), [55, 89, True])
test.assert_equals(product_fib(5895), [89, 144, False])
'''
def product_fib(_prod):
    fibonaccilist = [0, 1]
    fibonaccisum = 0
    fofncounter = 2
    while fibonaccisum <= _prod:
        fibonaccisum = fibonaccilist[fofncounter - 1] + fibonaccilist[fofncounter - 2]
        if fibonaccisum > _prod:
            break
        else:
            fibonaccilist.append(fibonaccisum)
            fofncounter += 1
    print(fibonaccilist) #print [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    fibonaccilistlength = len(fibonaccilist)
    for n in range(0, fibonaccilistlength - 1):
        print(fibonaccilist[n] * fibonaccilist[n + 1]) #print 0
        consecutiveproduct = fibonaccilist[n] * fibonaccilist[n + 1]
        if consecutiveproduct == _prod:
            return([fibonaccilist[n], fibonaccilist[n + 1], True])
        elif consecutiveproduct > _prod:
            return [fibonaccilist[n], fibonaccilist[n + 1], False]
        else:
            print([fibonaccilist[n], fibonaccilist[n + 1], False]) #print [0, 1, False]
            continue


print(product_fib(714)) #print [21, 34, True]
print(product_fib(800)) #print [34, 55, False]
print(product_fib(4895)) #print [55, 89, True]
print(product_fib(5895)) #print [89, 144, False]
print(product_fib(3)) #print [2, 3, False]

#Best solutions
def productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]

def productFib(prod):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, b + a
    return [a, b, a * b == prod]


#Google AI first page search result.  Find all factors for a multiplication product.
def extractfactors(number):
    factorslist = []
    for i in range(1, number + 1):
        if number % i == 0:
            factorslist.append(i)
    return factorslist


print(extractfactors(714)) #print [1, 2, 3, 6, 7, 14, 17, 21, 34, 42, 51, 102, 119, 238, 357, 714]
print(extractfactors(800)) #print [1, 2, 4, 5, 8, 10, 16, 20, 25, 32, 40, 50, 80, 100, 160, 200, 400, 800]

#https://docs.vultr.com/python/examples/find-the-factors-of-a-number
#This optimized function loops only up to the square root of num. Each time a factor is found, both i and num // i are added to the list (unless they are the same, in which case only one is added). The list is then sorted before returning.
import math
def find_factors_optimized(num):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)
    return sorted(factors)


print(find_factors_optimized(714)) #print [1, 2, 3, 6, 7, 14, 17, 21, 34, 42, 51, 102, 119, 238, 357, 714]
print(find_factors_optimized(800)) #print [1, 2, 4, 5, 8, 10, 16, 20, 25, 32, 40, 50, 80, 100, 160, 200, 400, 800]

#Generate a Fibonacci sequence list given the number of sequence
def fibonaccigenerator(sequence):
    fibonaccilist = [0, 1]
    fibonaccisum = 0
    for n in range(2, sequence + 1):
        fibonaccisum = fibonaccilist[n - 1] + fibonaccilist[n - 2]
        fibonaccilist.append(fibonaccisum)
    return fibonaccilist


print(fibonaccigenerator(19)) #print [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

#Trial function
product = 714
productlist = [1, 2, 3, 6, 7, 14, 17, 21, 34, 42, 51, 102, 119, 238, 357, 714]
fibonaccilist = [0, 1]
fibonaccisum = 0
fofncounter = 2
while fibonaccisum <= product:
    fibonaccisum = fibonaccilist[fofncounter - 1] + fibonaccilist[fofncounter - 2]
    if fibonaccisum >= product:
        break
    else:
        fibonaccilist.append(fibonaccisum)
        fofncounter += 1
print(fibonaccilist) #print [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
fibonaccilistlength = len(fibonaccilist)
for n in range(0, fibonaccilistlength - 1):
    print(fibonaccilist[n] * fibonaccilist[n + 1]) #print 714
    consecutiveproduct = fibonaccilist[n] * fibonaccilist[n + 1]
    if consecutiveproduct == product:
        print((fibonaccilist[n], fibonaccilist[n + 1], True)) #print (21, 34, True)
        break
    else:
        print((fibonaccilist[n], fibonaccilist[n + 1], False)) #print (0, 1, False).  For consecutiveproduct = 0.
