#https://www.codewars.com/kata/playing-on-a-chessboard
#6 Kyu
#With a friend we used to play the following game on a chessboard (8, rows, 8 columns). On the first row at the bottom we put numbers:  1/2, 2/3, 3/4, 4/5, 5/6, 6/7, 7/8, 8/9
#On row 2 (2nd row from the bottom) we have:  1/3, 2/4, 3/5, 4/6, 5/7, 6/8, 7/9, 8/10
#On row 3:  1/4, 2/5, 3/6, 4/7, 5/8, 6/9, 7/10, 8/11
#until last row:  1/9, 2/10, 3/11, 4/12, 5/13, 6/14, 7/15, 8/16
#When all numbers are on the chessboard each in turn we toss a coin. The one who get "head" wins and the other gives him, in dollars, the sum of the numbers on the chessboard. We play for fun, the dollars come from a monopoly game!
#How much can I (or my friend) win or loses for each game if the chessboard has n rows and n columns? Add all of the fractional values on an n by n sized board and give the answer as a simplified fraction.
#For Python, the function called 'game' with parameter n (integer >= 0) returns as result an irreducible fraction written as an array of integers: [numerator, denominator]. If the denominator is 1 return [numerator].
#test.assert_equals(game(0), [0])
#test.assert_equals(game(1), [1, 2])
#test.assert_equals(game(8), [32])

import numpy as np

# def game(n):
# 	chessboard = []
# 	for eachrow in range(1,n+1):
# 		chessboardrow = []
# 		for eachcolumn in range(1,n+1):
# 			#print("{} / {}+{}" .format(eachcolumn, eachrow, eachcolumn))
# 			#print(eachcolumn/(eachrow+eachcolumn))
# 			square = eachcolumn/(eachrow+eachcolumn)
# 			chessboardrow.append(square)
# 		chessboard.append(chessboardrow)
# 	#print(chessboard)
# 	chessboardarray = np.array(chessboard)
# 	print(np.sum(chessboardarray))
# game(0)
# game(1)
# game(8)
# #bonus insert a value at the end of an array https://github.com/numpy/numpy/issues/11705
# a = np.arange(4)
# print(a) # print [0 1 2 3]
# b = np.insert(a, len(a), values=9)
# print(b) #print [0 1 2 3 9]

size = 1
#https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python
from math import gcd  #from fractions import gcd
from functools import reduce #Needed for Python3.x
#uniquedenominators = [n for n in range(2,(size*2)+1)]
uniquedenominators = np.arange(2,(size*2)+1)
#print(uniquedenominators)
# def lcm(denominators):
# 	return reduce(lambda a,b: a*b // gcd(a,b), denominators)
# lowestcommonmultiple = lcm(uniquedenominators)
# print(lowestcommonmultiple)

# numeratorcolumn = np.array([n for n in range(1,size+1)]*size)
# denominatorrow = np.array([])
# dollars = []
# for row in range(1,size+1):
# 	for denominator in range(1,size+1):
# 		#denominatorrow.append(row+denominator)
# 		denominatorrow = np.append(denominatorrow, np.array([row+denominator]))
# for n in range(0,size*size):
# 	numeratorcolumn[n] = (lowestcommonmultiple//denominatorrow[n])*numeratorcolumn[n]
# numerator = np.sum([numeratorcolumn])
# denominator = lowestcommonmultiple
# if numerator % denominator == 0:
# 	dollars.append(numerator//denominator)
# else:
# 	dollars.append(numerator)
# 	dollars.append(denominator)	
# print(dollars)


def game(size):
	if size == 0:
		return [0]

	def lcm(denominators):
		return reduce(lambda a,b: a*b // gcd(a,b), denominators)	

	uniquedenominators = np.arange(2,(size*2)+1)
	lowestcommonmultiple = lcm(uniquedenominators)
	numeratorcolumn = np.array([n for n in range(1,size+1)]*size)
	denominatorrow = np.array([])
	dollars = []
	for row in range(1,size+1):
		for denominator in range(1,size+1):
			#denominatorrow.append(row+denominator)
			denominatorrow = np.append(denominatorrow, np.array([row+denominator]))
	for n in range(0,size*size):
		numeratorcolumn[n] = (lowestcommonmultiple//denominatorrow[n])*numeratorcolumn[n]
	numerator = np.sum([numeratorcolumn])
	denominator = lowestcommonmultiple
	if numerator % denominator == 0:
		dollars.append(numerator//denominator)
	else:
		dollars.append(numerator)
		dollars.append(denominator)	
	return dollars
print(game(0))
print(game(1))
print(game(3))
print(game(8))


#numpy method
# numerator = sum(numeratorcolumn)
# denominator = lowestcommonmultiple
# dollars = np.array([], dtype=np.int64)
# if numerator % denominator == 0:
# 	dollars = np.append(dollars, np.array([numerator//denominator]))
# else:
# 	dollars = np.append(dollars, np.array([numerator]))
# 	dollars = np.append(dollars, np.array([denominator]))
# print(dollars)


