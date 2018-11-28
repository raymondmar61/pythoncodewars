#https://www.codewars.com/kata/sum-of-digits-slash-digital-root
#In this kata, you must create a digital root function.  A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has two digits, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
'''
digital_root(16)
=> 1 + 6
=> 7
digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6
digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2
'''
def digital_root(n):
	n = list(str(n))
	while len(n) != 1:
		x = 0
		for eachn in n:
			x = int(eachn) + x
		if len(str(x)) == 1:
			print(x)
			break
		else:
			print(x)
			n = list(str(x))
digital_root(16)
digital_root(942)
digital_root(132189)
digital_root(493193)