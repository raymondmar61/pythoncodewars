#https://www.codewars.com/kata/574b3b1599d8f897470018f6/train/python
'''
What's the real floor? 8kyu

Americans are odd people: in their buildings, the first floor is actually the ground floor and there is no 13th floor (due to superstition).

Write a function that given a floor in the american system returns the floor in the european system.

With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take their place. In case of above 13, they move down by two because there are two omitted numbers below them.

Basements (negatives) stay the same as the universal level.

More information here

Examples
1  =>  0 
0  =>  0
5  =>  4
15  =>  13
-3  =>  -3
'''
def get_real_floor(n):
    if n <= 0:
        return (n)
    elif n <= 13:
        return (n - 1)
    elif n > 13:
        return (n - 2)


print(get_real_floor(1)) #print 0
print(get_real_floor(0)) #print 0
print(get_real_floor(5)) #print 4
print(get_real_floor(15)) #print 13
print(get_real_floor(-3)) #print -3

floornumber = 13
if floornumber <= 0:
    print(floornumber)
elif floornumber <= 13:
    print(floornumber - 1)
elif floornumber > 13:
    print(floornumber - 2) #print 12
