#https://www.codewars.com/kata/55d277882e139d0b6000005d/train/python
'''
Grasshopper - Array Mean 8 kyu

Find Mean
Find the mean (average) of a list of numbers in an array.

Information
To find the mean (average) of a set of numbers add all of the numbers together and divide by the number of values in the list.

For an example list of 1, 3, 5, 7

1. Add all of the numbers

1+3+5+7 = 16
2. Divide by the number of values in the list. In this example there are 4 numbers in the list.

16/4 = 4
3. The mean (or average) of this list is 4
'''
import statistics
def find_average(nums):
    return statistics.mean(nums)


print(find_average([1])) #print 1
print(find_average([1, 3, 5, 7])) #print 4
print(find_average([-1, 3, 5, -7])) #print 0
print(find_average([5, 7, 3, 7])) #print 5.5
print(find_average([0])) #print 0


listnumbers = [1, 3, 5, 7]
mean = sum(listnumbers) / len(listnumbers)
print(mean) #print 4.0
print(statistics.mean(listnumbers)) #print 4
listnumbers = [5, 7, 3, 7]
mean = sum(listnumbers) / len(listnumbers)
print(mean) #print 5.5
print(statistics.mean(listnumbers)) #print 5.5
