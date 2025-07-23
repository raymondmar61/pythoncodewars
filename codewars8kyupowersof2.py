#https://www.codewars.com/kata/57a083a57cb1f31db7000028/python
'''
Powers of 2 8kyu

Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

n = 0  ==> [1]        # [2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1]
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]
'''
def powers_of_two(n):
    return [pow(2, power) for power in range(0, n + 1)]


print(powers_of_two(0)) #print [1]
print(powers_of_two(1)) #print [1, 2]
print(powers_of_two(2)) #print [1, 2, 4]


n = 4
answerlist = []
for power in range(0, n + 1):
    answerlist.append(pow(2, power))
print(answerlist) #print [1, 2, 4, 8, 16]

#List comprehension
answerlist = [pow(2, power) for power in range(0, n + 1)]
print(answerlist) #print [1, 2, 4, 8, 16]
