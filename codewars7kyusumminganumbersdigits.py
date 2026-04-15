#https://www.codewars.com/kata/52f3149496de55aded000410/train/python
'''
Summing a number's digits 7 kyu

Write a function which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

For example: (Input --> Output)

10 --> 1
99 --> 18
-32 --> 5
Let's assume that all numbers in the input will be integer values.
'''
def sum_digits(number):
    splitnumber = list(str(abs(number)))
    sumnumberdigits = 0
    for eachsplitnumber in splitnumber:
        sumnumberdigits += int(eachsplitnumber)
    return sumnumberdigits


print(sum_digits(10)) #print 1
print(sum_digits(99)) #print 18
print(sum_digits(-32)) #print 5
print(sum_digits(1234567890)) #print 45
print(sum_digits(0)) #print 0
print(sum_digits(666)) #print 18
print(sum_digits(100000002)) #print 3
print(sum_digits(800000009)) #print 17

number = -32
print(abs(number)) #print 32
print(list(str(abs(number)))) #print ['3', '2']
splitnumber = list(str(abs(number)))
sumnumberdigits = 0
for eachsplitnumber in splitnumber:
    sumnumberdigits += int(eachsplitnumber)
print(sumnumberdigits) #print 5
