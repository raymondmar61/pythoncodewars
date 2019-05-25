#https://www.codewars.com/kata/maximum-subarray-sum
#5 Kyu earned
#The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
#maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
#should be 6: [4, -1, 2, 1]
#Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
#Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
from itertools import combinations, tee

#https://www.quora.com/How-do-I-iterate-through-a-list-in-python-while-comparing-the-values-at-adjacent-indices
# numberslist = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# love1, love2, love3 = tee(numberslist,3)
# print(love1) #print <itertools._tee object at 0x7f0b43ed1588>
# print(love2) #print <itertools._tee object at 0x7f0b43ed1588>
# print(love3) #print <itertools._tee object at 0x7f0b43ed1588>

#https://stackoverflow.com/questions/21303224/iterate-over-all-pairs-of-consecutive-items-in-a-list
# def nwise(lst, k=2):
#     return list(zip(*[lst[i:] for i in range(k)]))

def maxsequence(arr):
	maxlist = arr
	numberlistlength = len(maxlist)
	counter = 1
	maximumsumarray = 0
	if numberlistlength == 0:
		return 0
	positivecounter = 0
	negativecounter = 0
	for eachnumberslist in maxlist:
		if eachnumberslist >= 0:
			positivecounter+=1
		else:
			negativecounter+=1
	if positivecounter == numberlistlength:
		return (sum(maxlist))
	elif negativecounter == numberlistlength:
		return 0
	while counter <= numberlistlength:
		subarray = list(zip(*[maxlist[i:] for i in range(counter)]))
		for eachsubarray in subarray:
			sumarray = sum(list(eachsubarray))
			if sumarray > maximumsumarray:
				maximumsumarray = sumarray
		counter +=1
	return maximumsumarray
print(maxsequence([])) #print 0
print(maxsequence([1, 3, 5, 7])) #print 16
print(maxsequence([-1, -3, -5, -7])) #print 0
print(maxsequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])) #print 6
print(sum(list((1,2)))) #print 3
print(sum(list((15468,)))) #print 15468