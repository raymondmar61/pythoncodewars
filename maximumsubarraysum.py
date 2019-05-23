#https://www.codewars.com/kata/maximum-subarray-sum
#5 Kyu earned
#The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
#maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
#should be 6: [4, -1, 2, 1]
#Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
#Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
from itertools import combinations, tee
def maxsequence(numberslist):
	listlength = len(numberslist)
	if listlength == 0:
		return 0
	positivecounter = 0
	negativecounter = 0
	for eachnumberslist in numberslist:
		if eachnumberslist >= 0:
			positivecounter+=1
		else:
			negativecounter+=1
	if positivecounter == listlength:
		return (sum(numberslist))
	elif negativecounter == listlength:
		return 0
	maximumsum = 0
	# for n in range(1,listlength+1):
	# 	for combos in combinations(numberslist,n):
	# 		combossum = sum(list(combos))
	# 		if combossum > maximumsum:
	# 			maximumsum = combossum
	# return maximumsum
	#https://www.quora.com/How-do-I-iterate-through-a-list-in-python-while-comparing-the-values-at-adjacent-indices
	# love1, love2, love3 = tee(numberslist,3)
	# print(love1)
	# print(love2)
	# print(love3)

#https://stackoverflow.com/questions/21303224/iterate-over-all-pairs-of-consecutive-items-in-a-list
def maxSequence(arr):
	maxlist = arr
	maxlist = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	# def nwise(lst, k=2):
	#     return list(zip(*[lst[i:] for i in range(k)])) 
	#print(nwise(maxlist,3))
	# def nwise(numberlist):
	# 	numberlistlength = len(numberlist)
	# 	for n in range(1,numberlistlength+1):
	# 		print(list(zip*[numberlist[n:]]))
	#     #return list(zip(*[lst[i:] for i in range(k)])) 
	# nwise(maxlist)
	def nwise(lst, k=2):
	    return list(zip(*[lst[i:] for i in range(k)])) 
	numberlistlength = len(maxlist)
	counter = 1
	maximumsumarray = 0
	while counter <= numberlistlength:
		subarray = nwise(maxlist,counter)
		for eachsubarray in subarray:
			#print(eachsubarray)
			#print(sum(list(eachsubarray)))
			sumarray = sum(list(eachsubarray))
			if sumarray > maximumsumarray:
				maximumsumarray = sumarray
		counter +=1
	print("The answer is",maximumsumarray)


# print(maxsequence([]))
# print(maxsequence([1, 3, 5, 7]))
# print(maxsequence([-1, -3, -5, -7]))
# print(maxsequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(sum(list((1,2)))) #print 3
# print(sum(list((15468,)))) #print 15468