#https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python
'''
String repeat 8 kyu

Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated exactly n times.

Examples (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
'''
def repeat_str(repeat, string):
    return repeat * string


print(repeat_str(4, 'a')) #print 'aaaa'
print(repeat_str(3, 'hello ')) #print 'hello hello hello '
print(repeat_str(2, 'abc')) #print 'abcabc'
print(repeat_str(0, '')) #print ''
print(repeat_str(0, 'I')) #print ''
print(repeat_str(5, '')) #print ''
print(repeat_str(6, 'I')) #print 'IIIIII'
print(repeat_str(5, 'Hello')) #print 'HelloHelloHelloHelloHello'

print("I" * 6) #print IIIIII
print("Hello" * 5) #print HelloHelloHelloHelloHello