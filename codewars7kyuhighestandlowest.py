#https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
'''
Highest and Lowest 7kyu

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''
def high_and_low(numbers):
    stringtolist = numbers.split()
    stringintegerinlist = list(map(int, stringtolist))
    return (f"{str(max(stringintegerinlist))} {str(min(stringintegerinlist))}")


print(high_and_low("1 2 3 4 5")) #print 5 1
print(high_and_low("1 2 -3 4 5")) #print 5 -3
print(high_and_low("1 9 3 4 -5")) #print 9 -5
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")) #print 42 -9
print(high_and_low("1 2 3")) #print 3 1

numberstring = "1 2 3 4 5"
stringtolist = numberstring.split()
print(stringtolist) #print ['1', '2', '3', '4', '5']
stringintegerinlist = list(map(int, stringtolist))
print(stringintegerinlist) #print [1, 2, 3, 4, 5]
print(str(max(stringintegerinlist))) #print 5
print(str(min(stringintegerinlist))) #print 1
print("{} {}".format(str(max(stringintegerinlist)), str(min(stringintegerinlist)))) #print 5 1
print(f"{str(max(stringintegerinlist))} {str(min(stringintegerinlist))}") #print 5 1

#User submission
def high_and_low(numbers):
    numbers = [int(c) for c in numbers.split(' ')]
    return f"{max(numbers)} {min(numbers)}"