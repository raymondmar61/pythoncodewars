#https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python
'''
Calculate average 8kyu

Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0.
'''
def find_average(numbers):
    return sum(numbers) / len(numbers) if len(numbers) > 0 else 0


print(find_average([1, 2, 3])) #print 2.0
print(find_average([])) #print 0
print(find_average([1, 2])) #print 1.5

#Top submissions
def find_average(array):
    return sum(array) / len(array) if array else 0

def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0
