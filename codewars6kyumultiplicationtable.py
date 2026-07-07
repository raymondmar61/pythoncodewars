#https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python
'''
Multiplication table 6 kyu

Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9

For the given example, the return value should be:  [[1,2,3],[2,4,6],[3,6,9]]
'''
def multiplication_table(size):
    multiplier = 1
    solutionlist = []
    initialmultiplierlist = list(range(1, size + 1))
    while multiplier <= size:
        multiplierlist = [eachinitialmultiplierlist * multiplier for eachinitialmultiplierlist in initialmultiplierlist]
        solutionlist.append(multiplierlist)
        multiplier += 1
    return solutionlist


print(multiplication_table(1)) #print [[1]]
print(multiplication_table(2)) #print [[1, 2], [2, 4]]
print(multiplication_table(3)) #print [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
print(multiplication_table(4)) #print [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
print(multiplication_table(5)) #print [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

size = 3
multiplier = 1
solutionlist = []
initialmultiplierlist = list(range(1, size + 1))
while multiplier <= size:
    multiplierlist = [eachinitialmultiplierlist * multiplier for eachinitialmultiplierlist in initialmultiplierlist]
    solutionlist.append(multiplierlist)
    multiplier += 1

print(solutionlist) #print [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

#List comprehension.  Multiply each number inside list.  List multiply list.
numbers = [1, 2, 3, 4]
multiplier = 3
scaled_numbers = [num * multiplier for num in numbers]
print(scaled_numbers)  #print [3, 6, 9, 12]

size = 3
for n in range(1, size + 1):
    print(list(range(n, 4)))
    '''
    [1, 2, 3]
    [2, 3]
    [3]
    '''

#User solution
def multiplicationTable(size):
    return [[j * i for j in range(1, size + 1)] for i in range(1, size + 1)]
