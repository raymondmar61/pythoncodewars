#https://www.codewars.com/kata/find-the-odd-int, https://www.codewars.com/kata/find-the-odd-int/train/python
#6 Kyu earned
#Given an array, find the int that appears an odd number of times.
#There will always be only one integer that appears an odd number of times.
from collections import Counter
numberslist = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
print(Counter(numberslist)) #print Counter({5: 3, 20: 2, 1: 2, -1: 2, 2: 2, -2: 2, 3: 2, 4: 2})

from collections import Counter
def find_it(seq):
	counternumberslist = Counter(seq)
	for index, value in counternumberslist.items():
		if value % 2 != 0:
			return (index)
print(find_it(numberslist)) #print 5

#bonus basic Python
for x in numberslist:
	print(x, numberslist.count(x)) #count items in a list
	'''
	20 2
	1 2
	-1 2
	2 2
	-2 2
	3 2
	3 2
	5 3
	'''
	if numberslist.count(x) % 2 != 0:
		print(x) #print 5
		break