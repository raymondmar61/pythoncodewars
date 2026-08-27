#https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python
'''
Area or Perimeter 8 kyu

You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter.

Example(Input1, Input2 --> Output):

6, 10 --> 32
3, 3 --> 9
Note: for the purposes of this kata you will assume that it is a square if its length and width are equal, otherwise it is a rectangle.
'''
def area_or_perimeter(l, w):
    if l == w:
        return l**2
    else:
        return (l * 2) + (w * 2)


print(area_or_perimeter(4, 4)) #print 16
print(area_or_perimeter(6, 10)) #print 32
print(area_or_perimeter(3, 3)) #print 9

length = 4
width = 4
if length == width:
    print(length**2)
else:
    print((length * 2) + (width * 2)) #print 32

#User solution
def area_or_perimeter(l, w):
    return l * w if l == w else (l + w) * 2
