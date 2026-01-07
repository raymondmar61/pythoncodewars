#https://www.codewars.com/kata/58ca658cc0d6401f2700045f/train/python
'''
Find Multiples of a Number 8kyu

In this simple exercise, you will write a function that takes two integers; n and limit; and returns a list of the multiples of n up to and possibly including limit.  Multiples integer multiples number multiples.

It is guaranteed that n > 0 and limit >= n.

For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.

Examples
n = 2; limit = 6 --> [2, 4, 6]
n = 2; limit = 5 --> [2, 4]

Modulo or modulus.  Get the remainder from division.  Written with the percent sign %.  Takes a number and maps the number to a range based on the remainder when you divide the number.  number % modulus = remainder.  The remainder is always less than the modulus number.
'''
def find_multiples(integer, limit):
    multipleslist = []
    for eachlimit in range(1, limit + 1):
        if (eachlimit % integer) == 0:
            multipleslist.append(eachlimit)
    return multipleslist


print(find_multiples(2, 6)) #print [2, 4, 6]
print(find_multiples(2, 5)) #print [2, 4]
print(find_multiples(5, 25)) #print [5, 10, 15, 20, 25]
print(find_multiples(1, 2)) #print [1, 2]

#User solution
def find_multiples(integer, limit):
    return list(range(integer, limit + 1, integer))
