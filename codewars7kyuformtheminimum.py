#https://www.codewars.com/kata/5ac6932b2f317b96980000ca/train/python
'''
Form The Minimum 7kyu

Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once (ignore duplicates). Only positive integers in the range of 1 to 9 will be passed to the function.

Examples
[1, 3, 1] ==> 13
[5, 7, 5, 9, 7] ==> 579
[1, 9, 3, 1, 7, 4, 6, 6, 7]  ==> 134679
'''
def min_value(digits):
    digitslistnoduplicates = sorted(list(set(digits)))
    nocommasnumbers = ""
    for n in digitslistnoduplicates:
        nocommasnumbers = nocommasnumbers + "".join(str(n))
    return int(nocommasnumbers)


print(min_value([1, 3, 1])) #print 13
print(min_value([4, 7, 5, 7])) #print 457
print(min_value([4, 8, 1, 4])) #print 148
print(min_value([5, 7, 5, 9, 7])) #print 579
print(min_value([1, 9, 3, 1, 7, 4, 6, 6, 7])) #print 134679


print(set([1, 3, 1])) #print {1, 3}
print(set([5, 7, 5, 9, 7])) #print {9, 5, 7}
print(set([1, 9, 3, 1, 7, 4, 6, 6, 7])) #print {1, 3, 4, 6, 7, 9}
print(list((set([4, 8, 1, 4])))) #print [8, 1, 4]
print(sorted(list((set([4, 8, 1, 4]))))) #print [1, 4, 8]

#User submission
def min_value(digits):
    return int("".join(map(str, sorted(set(digits)))))
