#https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/train/python
'''
Sum of differences in array 8 kyu

Your task is to sum the differences between consecutive pairs in the array in descending order.

Example
[2, 1, 10]  -->  9
In descending order: [10, 2, 1]

Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9

If the array is empty or the array has only one element the result should be 0 (Nothing in Haskell, None in Rust).
'''
def sum_of_differences(arr):
    arrsorted = sorted(arr, reverse=True)
    numberslistcount = len(arrsorted)
    x = 0
    answer = 0
    while x < numberslistcount - 1:
        answer += arrsorted[x] - arrsorted[x + 1]
        x += 1
    return answer


print(sum_of_differences([1, 2, 10])) #print 9
print(sum_of_differences([-3, -2, -1])) #print 2
print(sum_of_differences([1, 1, 1, 1, 1])) #print 0
print(sum_of_differences([-17, 17])) #print 34
print(sum_of_differences([])) #print 0
print(sum_of_differences([0])) #print 0
print(sum_of_differences([-1])) #print 0
print(sum_of_differences([1])) #print 0

initialist = [1, 2, 10]
initiallistdescendingorder = sorted(initialist, reverse=True)
print(initiallistdescendingorder) #print [10, 2, 1]
print(len(initiallistdescendingorder)) #print 3
numberslistcount = len(initiallistdescendingorder)
x = 0
answer = 0
while x < numberslistcount - 1:
    print(initiallistdescendingorder[x]) #print 10
    print(initiallistdescendingorder[x + 1]) #print 2
    print(initiallistdescendingorder[x] - initiallistdescendingorder[x + 1]) #print 8
    answer += initiallistdescendingorder[x] - initiallistdescendingorder[x + 1]
    x += 1
print(answer) #print 9

#User submission
def sum_of_differences(arr):
    return max(arr) - min(arr) if arr else 0
