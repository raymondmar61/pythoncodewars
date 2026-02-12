#https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/train/python
'''
Reverse List Order 8kyu

In this kata you will create a function that takes in a list and returns a list with the reverse order.

Examples (Input -> Output)
* [1, 2, 3, 4]  -> [4, 3, 2, 1]
* [9, 2, 0, 7]  -> [7, 0, 2, 9]
'''
def reverse_list(l):
    return l[::-1]


print(reverse_list([1, 2, 3, 4])) #print [4, 3, 2, 1]
print(reverse_list([3, 1, 5, 4])) #print [4, 5, 1, 3]
print(reverse_list([3, 6, 9, 2])) #print [2, 9, 6, 3]
print(reverse_list([1])) #print [1]

forwardlist = [9, 2, 0, 7]
reverselist = forwardlist[::-1]
print(reverselist) #print [7, 0, 2, 9]
