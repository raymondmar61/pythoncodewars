#https://www.codewars.com/kata/56606694ec01347ce800001b/train/python
'''
Is this a triangle? 7kyu

Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

Examples:

Input -> Output
1,2,2 -> true
4,2,3 -> true
2,2,2 -> true
1,2,3 -> false
-5,1,3 -> false
0,2,3 -> false
1,2,9 -> false

Triangle Inequality Theorem.  Given three lengths a, b, and c.  The three lengths are a triangle if the sum of any two sides is greater than the third side.  If a+b>c, a+c>b, and b+c>a, then a, b, and c form a triangle.
'''
def is_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False


print(is_triangle(7, 2, 2)) #print False
print(is_triangle(1, 3, 2)) #print False
print(is_triangle(3, 1, 2)) #print False
print(is_triangle(5, 1, 2)) #print False
print(is_triangle(1, 2, 5)) #print False
print(is_triangle(2, 5, 1)) #print False
print(is_triangle(4, 2, 3)) #print True
print(is_triangle(5, 1, 5)) #print True
print(is_triangle(2, 2, 2)) #print True
print(is_triangle(-1, 2, 3)) #print False
print(is_triangle(1, -2, 3)) #print False
print(is_triangle(1, 2, -3)) #print False
print(is_triangle(0, 2, 3)) #print False

#User solution
def is_triangle(a, b, c):
    return all([a + b > c, a + c > b, b + c > a])
