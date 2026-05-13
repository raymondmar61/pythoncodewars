#https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/python
'''
Sum of Minimums! 7 kyu

Given a 2D ( nested ) list ( array, vector, .. ) of size m * n, your task is to find the sum of the minimum values in each row.

For Example:

[ [ 1, 2, 3, 4, 5 ]        #  minimum value of row is 1
, [ 5, 6, 7, 8, 9 ]        #  minimum value of row is 5
, [ 20, 21, 34, 56, 100 ]  #  minimum value of row is 20
]
So the function should return 26 because the sum of the minimums is 1 + 5 + 20 = 26.

Note: You will always be given a non-empty list containing positive values.

ENJOY CODING :)
'''
def sum_of_minimums(numbers):
    summinimumvalues = 0
    for eachnumbers in numbers:
        summinimumvalues += min(eachnumbers)
    return summinimumvalues


print(sum_of_minimums([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [20, 21, 34, 56, 100]])) #print 26
print(sum_of_minimums([[7, 9, 8, 6, 2], [6, 3, 5, 4, 3], [5, 8, 7, 4, 5]])) #print  9
print(sum_of_minimums([[11, 12, 14, 54], [67, 89, 90, 56], [7, 9, 4, 3], [9, 8, 6, 7]])) #print 76


twodimensionlist = [[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [20, 21, 34, 56, 100]]
summinimumvalues = 0
for eachtwodimensionlist in twodimensionlist:
    print(eachtwodimensionlist) #print [1, 2, 3, 4, 5]\n [5, 6, 7, 8, 9]\n [20, 21, 34, 56, 100]
    summinimumvalues += min(eachtwodimensionlist)
print(summinimumvalues) #print 26

#User submission
def sum_of_minimums(numbers):
    return sum(map(min, numbers))
