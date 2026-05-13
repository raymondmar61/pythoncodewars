#https://www.codewars.com/kata/5a03b3f6a1c9040084001765/train/python
'''
Sum of angles 7 kyu

Find the total sum of internal angles (in degrees) in an n-sided simple polygon. N will be greater than 2.

The sum of the interior angles of a polygon with sides is calculated using the formula:  sum = (n-2) * 180 degrees.  A triangle 3 sides is 180.  A square 4 sides is 360.  A pentagon 5 sides is 540.  A Hexagon 6 sides is 720.  A octagon 8 sides is 1080.
'''
def angle(n):
    return (n - 2) * 180


print(angle(3)) #print 180
print(angle(4)) #print 360
