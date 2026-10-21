#https://www.codewars.com/kata/58daa7617332e59593000006/train/python
'''
Most digits 7 kyu

Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.
'''
def find_longest(arr):
    numbersarraystring = [str(x) for x in arr]
    numbersarraystring.sort(key=len, reverse=True)
    return int(numbersarraystring[0])


print(find_longest([1, 10, 100])) #print 100
print(find_longest([9000, 8, 800])) #print 9000
print(find_longest([8, 900, 500])) #print 900
print(find_longest([3, 40000, 100])) #print 40000
print(find_longest([1, 200, 100000])) #print 100000
print(find_longest([10, 99, 11])) #print 10


numbersarray = [1, 10, 100, 200]
numbersarray = [8, 900, 500]
numbersarray = [10, 99, 11]
numbersarraystring = [str(x) for x in numbersarray]
print(numbersarraystring) #print ['10', '99', '11']
numbersarraystring.sort(key=len, reverse=True)
print(numbersarraystring) #print ['10', '99', '11']
print(numbersarraystring[0]) #print 10
