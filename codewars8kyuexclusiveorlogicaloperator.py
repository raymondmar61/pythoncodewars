#https://www.codewars.com/kata/56fa3c5ce4d45d2a52001b3c/train/python
'''
Exclusive "or" (xor) Logical Operator 8kyu

Overview
In some scripting languages like PHP, there exists a logical operator (e.g. &&, ||, and, or, etc.) called the "Exclusive Or" (hence the name of this Kata). The exclusive or evaluates two booleans. It then returns true if exactly one of the two expressions are true, false otherwise. For example:

false xor false == false // since both are false
true xor false == true // exactly one of the two expressions are true
false xor true == true // exactly one of the two expressions are true
true xor true == false // Both are true.  "xor" only returns true if EXACTLY one of the two expressions evaluate to true.

Task
Since we cannot define keywords in Javascript (well, at least I don't know how to do it), your task is to define a function xor(a, b) where a and b are the two expressions to be evaluated. Your xor function should have the behaviour described above, returning true if exactly one of the two expressions evaluate to true, false otherwise.
'''
def xor(a, b):
    if (a and b) and (a or b):
        return False
    else:
        return a or b


print(xor(False, False)) #print False
print(xor(True, False)) #print True
print(xor(False, True)) #print True
print(xor(True, True)) #print False
print("\n")

a = False
b = False
print(a or b) #print False
a = True
b = False
print(a or b) #print True
a = False
b = True
print(a or b) #print True
a = True
b = True
print(a or b) #print True
a = True
b = True
print((a or b) or (a and b)) #print True
print((a and b) and (a or b)) #print True
if (a and b) and (a or b):
    print("Should be False") #print Should be False

#User submissions
def xor(a, b):
    return a != b


'''
XOR function ^ caret function.  The caret ^ is a bitwise XOR; in other words, an exclusive OR.  XOR evalulates to True if and only if its arguments differ; in other words, one is True and the other is False.

XOR is exclusive or.  A binary operation.  There are 0s and 1s or zeros and ones in the binary system.  There are logical operators.  0 and 1 is zero.  1 and 0 is zero.  0 and 0 is zero.  1 and 1 is one.  0 or 1 is 1.  1 or 0 is 1.  1 or 1 is 1.  0 or 0 is 0.  1 xor 1 is 0.  xor must be different.
'''
def xor(a, b):
    return a ^ b
