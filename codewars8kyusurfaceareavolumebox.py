#https://www.codewars.com/kata/565f5825379664a26b00007c/train/python
'''
Surface Area and Volume of a Box 8 kyu

Write a function that returns the total surface area and volume of a box.  RM:  Formula for total surface area is 2(width*height) + 2(width*depth) + 2(height*depth).  Answer is units squared such as in^2 or cm^2.

The given input will be three positive non-zero integers: width, height, and depth.

The output will be language dependant, so please check sample tests for the corresponding data type, (list, tuple, struct, query, etcetera).
'''
def get_size(w, h, d):
    surfacearea = (2 * (w * h)) + (2 * (w * d)) + (2 * (h * d))
    volume = w * h * d
    return (surfacearea, volume)


print(get_size(4, 2, 6)) #print (88, 48)
print(get_size(1, 1, 1)) #print (6, 1)
print(get_size(1, 2, 1)) #print (10, 2)
print(get_size(1, 2, 2)) #print (16, 4)
print(get_size(10, 10, 10)) #print (600, 1000)


width = 4
height = 2
depth = 6
print((2 * (width * height)) + (2 * (width * depth)) + (2 * (height * depth))) #print 88
print(width * height * depth) #print 48
