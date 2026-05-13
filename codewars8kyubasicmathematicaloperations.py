#https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python
'''
Basic Mathematical Operations 8 kyu

Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
'''
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2


print(basic_op('+', 4, 7)) #print 11
print(basic_op('-', 15, 18)) #print -3
print(basic_op('*', 5, 5)) #print 25
print(basic_op('/', 49, 7)) #print 7

#User submission
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

def basic_op(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')
