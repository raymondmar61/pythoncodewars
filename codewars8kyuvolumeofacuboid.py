#https://www.codewars.com/kata/58261acb22be6e2ed800003a/train/python
'''
Volume of a Cuboid 8kyu

Bob needs a fast way to calculate the volume of a rectangular cuboid with three values: the length, width and height of the cuboid.

Write a function to help Bob with this calculation.
'''
def get_volume_of_cuboid(length, width, height):
    return int(length * width * height)


print(get_volume_of_cuboid(1, 2, 2)) #print 4
print(get_volume_of_cuboid(6.3, 2, 5)) #print 63
