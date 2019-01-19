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
			return x
		else:
			print(x)
			n = list(str(x))
print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
print(digital_root(7777))
print(digital_root(493193))
print(digital_root(99))

#a correct solution
#https://stackoverflow.com/questions/50278875/why-doesnt-this-digital-root-function-work
def digital_root(num):
    if num < 10:
        return num
    return digital_root(sum(map(int, str(num))))