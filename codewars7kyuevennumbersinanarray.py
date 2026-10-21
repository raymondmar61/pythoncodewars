#https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c/train/python
'''
Even numbers in an array 7 kyu

Given an array of numbers, return a new array of length number containing the last even numbers from the original array (in the same order). The original array will be not empty and will contain at least "number" even numbers.

For example:

([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) => [4, 6, 8]
([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2) => [-8, 26]
([6, -25, 3, 7, 5, 5, 7, -3, 23], 1) => [6]
'''
def even_numbers(arr, n):
    arrayevennumbers = []
    for eacharray in arr[::-1]:
        if eacharray % 2 == 0:
            arrayevennumbers.append(eacharray)
            n -= 1
        if n == 0:
            return arrayevennumbers[::-1]


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)) #print [4, 6, 8]
print(even_numbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2)) #print [-8, 26]
print(even_numbers([6, -25, 3, 7, 5, 5, 7, -3, 23], 1)) #print [6]

arraynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evennumberscount = 3
arrayevennumbers = []
for eacharraynumbers in arraynumbers[::-1]:
    if eacharraynumbers % 2 == 0:
        arrayevennumbers.append(eacharraynumbers)
        evennumberscount -= 1
    if evennumberscount == 0:
        break

print(arrayevennumbers[::-1]) #print [4, 6, 8]

#User solution
def even_numbers(arr, n):
    return [i for i in arr if i % 2 == 0][-n:]
