#https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
'''
Count of positives / sum of negatives 8 kyu

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
'''
def count_positives_sum_negatives(arr):
    positivecounter = 0
    negativesum = 0
    if not arr:
        return []
    for eacharr in arr:
        if eacharr > 0:
            positivecounter += 1
        elif eacharr < 0:
            negativesum += eacharr
        else:
            pass
    return [positivecounter, negativesum]


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])) #print [10,-65]
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14])) #print [8,-50]
print(count_positives_sum_negatives([1])) #print [1,0]
print(count_positives_sum_negatives([-1])) #print [0,-1]
print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0])) #print [0,0]
print(count_positives_sum_negatives([])) #print []

forinput = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
positivecounter = 0
negativesum = 0
for eachforinput in forinput:
    if eachforinput > 0:
        positivecounter += 1
    elif eachforinput < 0:
        negativesum += eachforinput
    else:
        pass

print([positivecounter, negativesum]) #print [10, -65]
