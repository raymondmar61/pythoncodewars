#https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python
#5 Kyu earned
#This time we want to write calculations using functions and get the results. Let's have a look at some examples:
'''
JavaScript:
seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3

Ruby:
seven(times(five)) # must return 35
four(plus(nine)) # must return 13
eight(minus(three)) # must return 5
six(divided_by(two)) # must return 3

Requirements:
There must be a function for each number from 0 ("zero") to 9 ("nine").
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby).
Each calculation consist of exactly one operation and two numbers.
The most outer function represents the left operand, the most inner function represents the right operand.
Divison should be integer division, e.g eight(dividedBy(three()))/eight(divided_by(three)) should return 2, not 2.666666....
'''
#https://stackoverflow.com/questions/9752958/how-can-i-return-two-values-from-a-function-in-python
#answer you cannot return two values.  You can return a tuple or a list follow by unpacking afterwards.
def pluscantreturntwovalues(firstnumber):
	operator = "plus"
	return operator
def plusCANreturntwovalues(firstnumber):
	operator = "plus"
	return [firstnumber, operator]
print(pluscantreturntwovalues(5)) #print plus
print(plusCANreturntwovalues(5)) #print [5, 'plus']

#anter69
def zero(arg=""):
	return eval("0" + arg)
def one(arg=""):
	return eval("1" + arg)
def two(arg=""):
	return eval("2" + arg)
def three(arg=""):
	return eval("3" + arg)
def four(arg=""):
	return eval("4" + arg)
def five(arg=""):
	return eval("5" + arg)
def six(arg=""):
	return eval("6" + arg)
def seven(arg=""):
	return eval("7" + arg)
def eight(arg=""):
	return eval("8" + arg)
def nine(arg=""):
	return eval("9" + arg)
def plus(n):
	return "+%s" % n #%s converts to string
def minus(n):
	return "-%s" % n
def times(n):	
	return "*%s" % n
def divided_by(n):
	return "//%s" % n
print(seven()) #print 7
print(times(seven())) #print *7
print(five(times(seven()))) #print 35
print("*%s") #print %s
n = 7
print("*%s" % n) #print *7
arg = "*%s" % n
print(eval("5" + arg)) #print 35
print(eval(str(345) + "-300")) #print 45

#jslpmec
def zero(x = None):
    if x == None:
        return 0
    else:
        if x[0] == '+':
            return 0 + x[1]
        elif x[0] == '-':
            return 0 - x[1]
        elif x[0] == '*':
            return 0 * x[1]
        elif x[0] == '/':
            return 0 // x[1]
def one(x = None):
    if x == None:
        return 1
    else:
        if x[0] == '+':
            return 1 + x[1]
        elif x[0] == '-':
            return 1 - x[1]
        elif x[0] == '*':
            return 1 * x[1]
        elif x[0] == '/':
            return 1 // x[1]
def two(x = None):
    if x == None:
        return 2
    else:
        if x[0] == '+':
            return 2 + x[1]
        elif x[0] == '-':
            return 2 - x[1]
        elif x[0] == '*':
            return 2 * x[1]
        elif x[0] == '/':
            return 2 // x[1]
def three(x = None):
    if x == None:
        return 3
    else:
        if x[0] == '+':
            return 3 + x[1]
        elif x[0] == '-':
            return 3 - x[1]
        elif x[0] == '*':
            return 3 * x[1]
        elif x[0] == '/':
            return 3 // x[1]
def four(x = None):
    if x == None:
        return 4
    else:
        if x[0] == '+':
            return 4 + x[1]
        elif x[0] == '-':
            return 4 - x[1]
        elif x[0] == '*':
            return 4 * x[1]
        elif x[0] == '/':
            return 4 // x[1]
def five(x = None):
    if x == None:
        return 5
    else:
        if x[0] == '+':
            return 5 + x[1]
        elif x[0] == '-':
            return 5 - x[1]
        elif x[0] == '*':
            return 5 * x[1]
        elif x[0] == '/':
            return 5 // x[1]
def six(x = None):
    if x == None:
        return 6
    else:
        if x[0] == '+':
            return 6 + x[1]
        elif x[0] == '-':
            return 6 - x[1]
        elif x[0] == '*':
            return 6 * x[1]
        elif x[0] == '/':
            return 6 // x[1]
def seven(x = None):
    if x == None:
        return 7
    else:
        if x[0] == '+':
            return 7 + x[1]
        elif x[0] == '-':
            return 7 - x[1]
        elif x[0] == '*':
            return 7 * x[1]
        elif x[0] == '/':
            return 7 // x[1]
def eight(x = None):
    if x == None:
        return 8
    else:
        if x[0] == '+':
            return 8 + x[1]
        elif x[0] == '-':
            return 8 - x[1]
        elif x[0] == '*':
            return 8 * x[1]
        elif x[0] == '/':
            return 8 // x[1]
def nine(x = None):
    if x == None:
        return 9
    else:
        if x[0] == '+':
            return 9 + x[1]
        elif x[0] == '-':
            return 9 - x[1]
        elif x[0] == '*':
            return 9 * x[1]
        elif x[0] == '/':
            return 9 // x[1]
def plus(x):
    return ('+', x)
def minus(x):
    return ('-', x)
def times(x):
    return ('*', x)
def divided_by(x):
    return ('/', x)
print(three()) #print 3
print(minus(three())) #print ('-', 3)
print(nine(minus(three()))) #print 6
tuplecheck = ("first position",2)
print(tuplecheck[0]) #print first position
print(tuplecheck[1]) #print 2

#Bergi
def zero(input=None):
    n = 0
    if input == None:
        return(n)
    elif input[0] == "+":
        return(int(n+input[1]))
    elif input[0] == "-":
        return(int(n-input[1]))
    elif input[0] == "*":
        return(int(n*input[1]))
    elif input[0] == "/":
        return(int(n/input[1]))        
def one(input=None):
    n = 1
    if input == None:
        return(n)
    elif input[0] == "+":
        return(int(n+input[1]))
    elif input[0] == "-":
        return(int(n-input[1]))
    elif input[0] == "*":
        return(int(n*input[1]))
    elif input[0] == "/":
        return(int(n/input[1]))        
def two(input=None):
    n = 2
    if input == None:
        return(n)
    elif input[0] == "+":
        return(int(n+input[1]))
    elif input[0] == "-":
        return(int(n-input[1]))
    elif input[0] == "*":
        return(int(n*input[1]))
    elif input[0] == "/":
        return(int(n/input[1]))        
def three(input=None):
    n = 3
    if input == None:
        return(n)
    elif input[0] == "+":
        return(int(n+input[1]))
    elif input[0] == "-":
        return(int(n-input[1]))
    elif input[0] == "*":
        return(int(n*input[1]))
    elif input[0] == "/":
        return(int(n/input[1]))        
def four(input=None):
    n = 4
    if input == None:
        return(n)
    elif input[0] == "+":
        return(int(n+input[1]))
    elif input[0] == "-":
        return(int(n-input[1]))
    elif input[0] == "*":
        return(int(n*input[1]))
    elif input[0] == "/":
        return(int(n/input[1]))        
def five(input=None):
    n = 5
    if input == None:
        return(n)
    elif input[0] == "+":
        return(int(n+input[1]))
    elif input[0] == "-":
        return(int(n-input[1]))
    elif input[0] == "*":
        return(int(n*input[1]))
    elif input[0] == "/":
        return(int(n/input[1]))
def six(input=None):
    n = 6
    if input == None:
        return(n)
    elif input[0] == "+":
        return(int(n+input[1]))
    elif input[0] == "-":
        return(int(n-input[1]))
    elif input[0] == "*":
        return(int(n*input[1]))
    elif input[0] == "/":
        return(int(n/input[1]))        
def seven(input=None):
    n = 7
    if input == None:
        return(n)
    elif input[0] == "+":
        return(int(n+input[1]))
    elif input[0] == "-":
        return(int(n-input[1]))
    elif input[0] == "*":
        return(int(n*input[1]))
    elif input[0] == "/":
        return(int(n/input[1]))        
def eight(input=None):
    n = 8
    if input == None:
        return(n)
    elif input[0] == "+":
        return(int(n+input[1]))
    elif input[0] == "-":
        return(int(n-input[1]))
    elif input[0] == "*":
        return(int(n*input[1]))
    elif input[0] == "/":
        return(int(n/input[1]))
def nine(input=None):
    n = 9
    if input == None:
        return(n)
    elif input[0] == "+":
        return(int(n+input[1]))
    elif input[0] == "-":
        return(int(n-input[1]))
    elif input[0] == "*":
        return(int(n*input[1]))
    elif input[0] == "/":
        return(int(n/input[1]))
def plus(input):
    return(["+",input])
def minus(input):
    return(["-",input])
def times(input):
    return(["*",input])
def divided_by(input):
    return(["/",input])
print(eight()) #print 8
print(divided_by(eight())) #print ['/', 8]
print(eight(divided_by(two()))) #print 4
listcheck = ['/', 8]
print(listcheck[0]) #print /
print(listcheck[1]) #print 8

def zero(secondnumber_operator=None):
	firstnumber = 0
	if secondnumber_operator is None:
		return firstnumber
	elif secondnumber_operator[1] == "plus":
		return firstnumber + secondnumber_operator[0]
	elif secondnumber_operator[1] == "minus":
		return firstnumber - secondnumber_operator[0]
	elif secondnumber_operator[1] == "times":
		return firstnumber * secondnumber_operator[0]
	elif secondnumber_operator[1] == "dividedby":
		return firstnumber // secondnumber_operator[0]
def one(secondnumber_operator=None):
	firstnumber = 1
	if secondnumber_operator is None:
		return firstnumber
	elif secondnumber_operator[1] == "plus":
		return firstnumber + secondnumber_operator[0]
	elif secondnumber_operator[1] == "minus":
		return firstnumber - secondnumber_operator[0]
	elif secondnumber_operator[1] == "times":
		return firstnumber * secondnumber_operator[0]
	elif secondnumber_operator[1] == "dividedby":
		return firstnumber // secondnumber_operator[0]
def two(secondnumber_operator=None):
	firstnumber = 2
	if secondnumber_operator is None:
		return firstnumber
	elif secondnumber_operator[1] == "plus":
		return firstnumber + secondnumber_operator[0]
	elif secondnumber_operator[1] == "minus":
		return firstnumber - secondnumber_operator[0]
	elif secondnumber_operator[1] == "times":
		return firstnumber * secondnumber_operator[0]
	elif secondnumber_operator[1] == "dividedby":
		return firstnumber // secondnumber_operator[0]
def three(secondnumber_operator=None):
	firstnumber = 3
	if secondnumber_operator is None:
		return firstnumber
	elif secondnumber_operator[1] == "plus":
		return firstnumber + secondnumber_operator[0]
	elif secondnumber_operator[1] == "minus":
		return firstnumber - secondnumber_operator[0]
	elif secondnumber_operator[1] == "times":
		return firstnumber * secondnumber_operator[0]
	elif secondnumber_operator[1] == "dividedby":
		return firstnumber // secondnumber_operator[0]
def four(secondnumber_operator=None):
	firstnumber = 4
	if secondnumber_operator is None:
		return firstnumber
	elif secondnumber_operator[1] == "plus":
		return firstnumber + secondnumber_operator[0]
	elif secondnumber_operator[1] == "minus":
		return firstnumber - secondnumber_operator[0]
	elif secondnumber_operator[1] == "times":
		return firstnumber * secondnumber_operator[0]
	elif secondnumber_operator[1] == "dividedby":
		return firstnumber // secondnumber_operator[0]
def five(secondnumber_operator=None):
	firstnumber = 5
	if secondnumber_operator is None:
		return firstnumber
	elif secondnumber_operator[1] == "plus":
		return firstnumber + secondnumber_operator[0]
	elif secondnumber_operator[1] == "minus":
		return firstnumber - secondnumber_operator[0]
	elif secondnumber_operator[1] == "times":
		return firstnumber * secondnumber_operator[0]
	elif secondnumber_operator[1] == "dividedby":
		return firstnumber // secondnumber_operator[0]
def six(secondnumber_operator=None):
	firstnumber = 6
	if secondnumber_operator is None:
		return firstnumber
	elif secondnumber_operator[1] == "plus":
		return firstnumber + secondnumber_operator[0]
	elif secondnumber_operator[1] == "minus":
		return firstnumber - secondnumber_operator[0]
	elif secondnumber_operator[1] == "times":
		return firstnumber * secondnumber_operator[0]
	elif secondnumber_operator[1] == "dividedby":
		return firstnumber // secondnumber_operator[0]
def seven(secondnumber_operator=None):
	firstnumber = 7
	if secondnumber_operator is None:
		return firstnumber
	elif secondnumber_operator[1] == "plus":
		return firstnumber + secondnumber_operator[0]
	elif secondnumber_operator[1] == "minus":
		return firstnumber - secondnumber_operator[0]
	elif secondnumber_operator[1] == "times":
		return firstnumber * secondnumber_operator[0]
	elif secondnumber_operator[1] == "dividedby":
		return firstnumber // secondnumber_operator[0]
def eight(secondnumber_operator=None):
	firstnumber = 8
	if secondnumber_operator is None:
		return firstnumber
	elif secondnumber_operator[1] == "plus":
		return firstnumber + secondnumber_operator[0]
	elif secondnumber_operator[1] == "minus":
		return firstnumber - secondnumber_operator[0]
	elif secondnumber_operator[1] == "times":
		return firstnumber * secondnumber_operator[0]
	elif secondnumber_operator[1] == "dividedby":
		return firstnumber // secondnumber_operator[0]
def nine(secondnumber_operator=None):
	firstnumber = 9
	if secondnumber_operator is None:
		return firstnumber
	elif secondnumber_operator[1] == "plus":
		return firstnumber + secondnumber_operator[0]
	elif secondnumber_operator[1] == "minus":
		return firstnumber - secondnumber_operator[0]
	elif secondnumber_operator[1] == "times":
		return firstnumber * secondnumber_operator[0]
	elif secondnumber_operator[1] == "dividedby":
		return firstnumber // secondnumber_operator[0]
def plus(firstnumber):
	return [firstnumber,"plus"]
def minus(firstnumber):
	return [firstnumber,"minus"]
def times(firstnumber):
	return [firstnumber,"times"]
def dividedby(firstnumber):
	return [firstnumber,"dividedby"]
print(one()) #print 1
print(plus(one())) #print [1, 'plus']
print(zero(plus(one()))) #print 1
print(five(plus(one()))) #print 6
print(eight(minus(three()))) #print 5
print(nine(dividedby(four()))) #print 2
print(six(dividedby(two()))) #print 3