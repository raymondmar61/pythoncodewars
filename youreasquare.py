#https://www.codewars.com/kata/youre-a-square
#You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!
#However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.
#Given an integral number, determine if it's a square number:  In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
#The tests will always use some integral number, so don't worry about that in dynamic typed languages.
#RM:  I cheated converting integer to string
from math import sqrt

def issquare(n):
	if n < 0:
		return False
	else:
		number = str(sqrt(n))
	if number[-1] == "0" and number[-2] == ".":
		return True
		#return ("{} is a square number".format(n))
	else:
		#return ("{} is not a square number".format(n))
		return False

print(issquare(-1)) #print False
print(issquare(0)) #print True
print(issquare(3)) #print False
print(issquare(4)) #print True
print(issquare(25)) #print True
print(issquare(26)) #print False

#https://stackoverflow.com/questions/44531084/python-check-if-a-number-is-a-square
def is_square(n):
    if n<1:
        return False
    else:
        for i in range(int(n/2)+1):
            if (i*i)==n:
                return True
        return False
print(is_square(-1)) #print False
print(is_square(100)) #print True
print(is_square(1001)) #print False

def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    x, y = 1, n
    while x + 1 < y:
        mid = (x+y)//2
        if mid**2 < n:
            x = mid
        else:
            y = mid
    return n == x**2 or n == (x+1)**2
print(is_square(-1)) #print False
print(is_square(100)) #print True
print(is_square(1001)) #print False