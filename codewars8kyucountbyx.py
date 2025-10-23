#https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
'''
Count by X 8kyu

Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).

Examples
x = 1, n = 10 --> [1,2,3,4,5,6,7,8,9,10]
x = 2, n = 5  --> [2,4,6,8,10]
'''
def count_by(x, n):
    answer = 0
    answerarray = []
    for counter in range(0, n):
        answer = x + answer
        answerarray.append(answer)
    return answerarray


print(count_by(1, 10)) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(count_by(1, 5)) #print [1, 2, 3, 4, 5]
print(count_by(2, 5)) #print [2, 4, 6, 8, 10]
print(count_by(3, 5)) #print [3, 6, 9, 12, 15]
print(count_by(50, 5)) #print [50, 100, 150, 200, 250]
print(count_by(100, 5)) #print [100, 200, 300, 400, 500]

start = 50
ntimes = 5
answer = 0
answerarray = []
for counter in range(0, ntimes):
    answer = start + answer
    print(answer) #print 50\n 100\n 150\n 200\n 250\n
    answerarray.append(answer)
print(answerarray) #print [50, 100, 150, 200, 250]

start = 50
ntimes = 5
listcomprehension = [counter * start for counter in range(1, ntimes + 1)]
print(listcomprehension) #print [50, 100, 150, 200, 250]
