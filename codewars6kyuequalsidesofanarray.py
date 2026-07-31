#https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python
'''
Equal Sides Of An Array 6 kyu

You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N.

If there is no index that would make this happen, return -1.

For example:
Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}:
Your function will return the index 1, because the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

Last one:
You are given the array {20,10,-80,10,10,15,35}
At index 0 the left side is {}
The right side is {10,-80,10,10,15,35}
They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
Index 0 is the place where the left side and right side are equal.

Note: Please remember that in most languages the index of an array starts at 0.

Input
An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

Output
The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.

Note
If you are given an array with multiple answers, return the lowest correct index.
'''
def find_even_index(arr):
    if sum(arr[1:]) == 0:
        return 0
    arrlength = len(arr)
    for x in range(0, arrlength):
        if sum(arr[0:x]) == sum(arr[:x:-1]):
            return x
    return -1


print(find_even_index([20, 10, -80, 10, 10, 15, 35])) #print 0
print(find_even_index([1, 2, 3, 4, 3, 2, 1])) #print 3
print(find_even_index([1, 100, 50, -51, 1, 1])) #print 1
print(find_even_index([1, 2, 3, 4, 3, 2, 1])) #print 3
print(find_even_index([1, 100, 50, -51, 1, 1])) #print 1
print(find_even_index([1, 2, 3, 4, 5, 6])) #print -1
print(find_even_index([20, 10, 30, 10, 10, 15, 35])) #print 3
print(find_even_index([20, 10, -80, 10, 10, 15, 35])) #print 0
print(find_even_index([10, -80, 10, 10, 15, 35, 20])) #print 6
print(find_even_index(list(range(1, 100)))) #print -1
print(find_even_index([0, 0, 0, 0, 0])) #print 0
print(find_even_index([-1, -2, -3, -4, -3, -2, -1])) #print 3
print(find_even_index(list(range(-100, -1)))) #print -1
print(find_even_index([8, 8])) #print -1
print(find_even_index([8, 0])) #print 0
print(find_even_index([0, 8])) #print 1
print(find_even_index([7, 3, -3])) #print 0
print(find_even_index([8])) #print 0
print(find_even_index([10, -10])) #print -1
print(find_even_index([-3, 2, 1, 0])) #print 3
print(find_even_index([-15, 5, 11, 17, 19, -17, 20, -6, 17, -17, 19, 16, -15, -6, 20, 17])) #print 8


givenarray = [1, 100, 50, -51, 1, 1]
givenarray = [1, 2, 3, 4, 3, 2, 1]
givenarraylength = len(givenarray)
print(givenarraylength) #print 7
print(givenarray[1:]) #print [2, 3, 4, 3, 2, 1]
print(sum(givenarray[1:])) #print 15
for x in range(0, givenarraylength):
    print("x value", x)
    print(givenarray[0:x])
    print(givenarray[0:x], givenarray[:x:-1])
    print(sum(givenarray[0:x]), sum(givenarray[:x:-1]), sum(givenarray[0:x]) == sum(givenarray[:x:-1]))
    '''
    x value 0
    []
    [] [1, 2, 3, 4, 3, 2]
    0 15 False
    x value 1
    [1]
    [1] [1, 2, 3, 4, 3]
    1 13 False
    x value 2
    [1, 2]
    [1, 2] [1, 2, 3, 4]
    3 10 False
    x value 3
    [1, 2, 3]
    [1, 2, 3] [1, 2, 3]
    6 6 True
    x value 4
    [1, 2, 3, 4]
    [1, 2, 3, 4] [1, 2]
    10 3 False
    x value 5
    [1, 2, 3, 4, 3]
    [1, 2, 3, 4, 3] [1]
    13 1 False
    x value 6
    [1, 2, 3, 4, 3, 2]
    [1, 2, 3, 4, 3, 2] []
    15 0 False
    '''

givenarray = [20, 10, -80, 10, 10, 15, 35]
print(givenarray[1:]) #print [10, -80, 10, 10, 15, 35]
if sum(givenarray[1:]) == 0:
    print(0) #print 0

#User solution
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1
