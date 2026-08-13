#https://www.codewars.com/kata/5708f682c69b48047b000e07/train/python
'''
Multiply the number 8 kyu

Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:

  3 -->    15  (  3 * 5¹)
 10 -->   250  ( 10 * 5²)
200 --> 25000  (200 * 5³)
  0 -->     0  (  0 * 5¹)
 -3 -->   -15  ( -3 * 5¹)
'''
def multiply(n):
    return n * pow(5, len(str(abs(n))))


print(multiply(10)), #print 250
print(multiply(5)), #print 25
print(multiply(200)), #print 25000
print(multiply(0)), #print 0
print(multiply(-2)), #print -10
print(multiply(3)), #print 15
print(multiply(-3)), #print -15


inputnumber = 200
power = len(str(inputnumber))
print(inputnumber * pow(5, power)) #print 25000
