#https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
'''
Persistent Bugger.  6kyu

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)
'''

def persistence(n):
    persistencelength = len(str(n))
    counter = 0
    while persistencelength > 1:
        counter += 1
        numbertostring = str(n)
        numbertostringlist = [*numbertostring]
        product = 1
        for eachnumbertostringlist in numbertostringlist:
            product = int(eachnumbertostringlist) * product
        persistencelength = len(str(product))
        n = product
    return counter


print(persistence(39)) #print 3
print(persistence(4)) #print 0
print(persistence(25)) #print 2
print(persistence(999)) #print 4

#Separate integers split integers to string.  First convert integer to a string.  givennumber = 70304 givennumberstring = str(givennumber) givennumberlist = [*givennumberstring] print(givennumberlist) #print ['7', '0', '3', '0', '4'].
number = 123456789
stringeachnumber = [*str(number)]
print(stringeachnumber) #print ['1', '2', '3', '4', '5', '6', '7', '8', '9']
number = 999
numbertostring = str(number)
numbertostringlist = [*numbertostring]
print(numbertostringlist) #print ['9', '9', '9']
product = 1
for eachnumbertostringlist in numbertostringlist:
    product = int(eachnumbertostringlist) * product
    print(product) #print 9\n 81\n 729
number = 729
numbertostring = str(number)
numbertostringlist = [*numbertostring]
print(numbertostringlist) #print ['7', '2', '9']
product = 1
for eachnumbertostringlist in numbertostringlist:
    product = int(eachnumbertostringlist) * product
    print(product) #print 7\n 14\n 126
number = 126
numbertostring = str(number)
numbertostringlist = [*numbertostring]
print(numbertostringlist) #print ['1', '2', '6']
product = 1
for eachnumbertostringlist in numbertostringlist:
    product = int(eachnumbertostringlist) * product
    print(product) #print 1\n 2\n 12
number = 12
numbertostring = str(number)
numbertostringlist = [*numbertostring]
print(numbertostringlist) #print ['1', '2']
product = 1
for eachnumbertostringlist in numbertostringlist:
    product = int(eachnumbertostringlist) * product
    print(product) #print 1\n 2
