#https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python
'''
Find the next perfect square!

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative.

Examples ( Input --> Output )
121 --> 144
625 --> 676
114 --> -1  #  because 114 is not a perfect square
'''
import math
def find_next_square(sq):
    squareroot = math.sqrt(sq)
    squareroot += 1
    squareroot = pow(squareroot, 2)
    if math.sqrt(squareroot) % 1 == 0:
        return int(squareroot)
    else:
        return -1


print(find_next_square(121)) #print 144
print(find_next_square(625)) #print 676
print(find_next_square(114)) #print -1
