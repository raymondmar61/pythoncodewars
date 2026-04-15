#https://www.codewars.com/kata/586f6741c66d18c22800010a/train/python
'''
Sum of a sequence 7 kyu

Your task is to write a function which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, your function should return 0. If end is not the result of an integer number of steps, then don't add it to the sum. See the 4th example below.

Examples

2,2,2 --> 2
2,6,2 --> 12 (2 + 4 + 6)
1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
1,5,3 --> 5 (1 + 4)
'''
def sequence_sum(begin_number, end_number, step):
    numberlist = list(range(begin_number, end_number + 1, step))
    return sum(numberlist)


print(sequence_sum(2, 6, 2)) #print 12
print(sequence_sum(1, 5, 1)) #print 15
print(sequence_sum(1, 5, 3)) #print 5
print(sequence_sum(0, 15, 3)) #print 45
print(sequence_sum(16, 15, 3)) #print 0
print(sequence_sum(2, 24, 22)) #print 26
print(sequence_sum(2, 2, 2)) #print 2
print(sequence_sum(2, 2, 1)) #print 2
print(sequence_sum(1, 15, 3)) #print 35
print(sequence_sum(15, 1, 3)) #print 0

numberlist = list(range(1, 5 + 1, 1))
print(numberlist) #print [1, 2, 3, 4, 5]
print(sum(numberlist)) #print 15
numberlist = list(range(1, 5 + 1, 3))
print(numberlist) #print [1, 2, 3, 4, 5]
