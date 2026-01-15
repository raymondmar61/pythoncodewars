#https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python
'''
Sum The Strings 8kyu

Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

Example: (Input1, Input2 -->Output)

"4",  "5" --> "9"
"34", "5" --> "39"
"", "" --> "0"
"2", "" --> "2"
"-5", "3" --> "-2"
Notes:

If either input is an empty string, consider it as zero.

Inputs and the expected output will never exceed the signed 32-bit integer limit (2^31 - 1)

'''
def sum_str(a, b):
    if a == "":
        a = 0
    if b == "":
        b = 0
    return ("{}".format(int(a) + int(b)))


print(sum_str("4", "5")) #print 9
print(sum_str("34", "5")) #print 39
print(sum_str("", "")) #print 0
print(sum_str("2", "")) #print 2
print(sum_str("-5", "3")) #print -2
print(sum_str("9", "")) #print 9
print(sum_str("", "9")) #print 9
print(sum_str("", "")) #print 0


print("Sum {}".format(3 + 4)) #print Sum 7
print("{}".format(3 + 4)) #print 7
print(type("{}".format(3 + 4))) #print <class 'str'>

print("Sum {}".format(int("3") + int("4"))) #print Sum 7
print("{}".format(int("3") + int("4"))) #print 7
print(type("{}".format(int("3") + int("4")))) #print <class 'str'>

#User submissions
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))

def sum_str(a, b):
    return str(int('0' + a) + int('0' + b))
