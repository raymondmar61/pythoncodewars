#https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python
'''
Ones and Zeros 7 kyu

Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11

However, the arrays can have varying lengths, not just limited to 4.
'''
def binary_array_to_number(arr):
    binaryarraytostring = list(map(str, arr))
    binaryvalue = ("".join((binaryarraytostring)))
    return int(binaryvalue, 2) #int() function converts the binary string back to an integer using base 2 or binary.  Input must be a string.


print(binary_array_to_number([0, 0, 0, 1])) #print 1
print(binary_array_to_number([0, 0, 1, 0])) #print 2
print(binary_array_to_number([1, 1, 1, 1])) #print 15
print(binary_array_to_number([0, 1, 1, 0])) #print 6
print(binary_array_to_number([0, 1, 0, 1])) #print 5
print(binary_array_to_number([1, 0, 0, 1])) #print 9
print(binary_array_to_number([1, 0, 1, 1])) #print 11

binaryarray = [1, 0, 1, 1]
binaryarraytostring = list(map(str, binaryarray))
print(binaryarraytostring) #print ['1', '0', '1', '1']
binaryvalue = ("".join((binaryarraytostring)))
print(binaryvalue) #print 1011
print(type(binaryvalue)) #print <class 'str'>
print(int(binaryvalue, 2)) #print 11.  int() function converts the binary string back to an integer using base 2 or binary.  Input must be a string.
