#https://www.codewars.com/kata/5783d8f3202c0e486c001d23/train/python
'''
Convert an array of strings to array of numbers 7 kyu

Oh no!
Some really funny web dev gave you a sequence of numbers from his API response as an sequence of strings!

You need to cast the whole array to the correct type.

Create the function that takes as a parameter a sequence of numbers represented as strings and outputs a sequence of numbers.

ie:["1", "2", "3"] to [1, 2, 3]

Note that you can receive floats as well.
'''
def to_float_array(arr):
    isdecimalpresent = arr[0].find(".")
    if isdecimalpresent >= 0:
        return [float(x) for x in arr]
    else:
        return [int(x) for x in arr]


print(to_float_array(["1.0", "2.0", "3.0"])) #print [1.0, 2.0, 3.0]
print(to_float_array(["1", "2", "3"])) #print [1, 2, 3]


sequencestringnumbers = ["1.0", "2.0", "3.0"]
sequencestringnumbers = ["1", "2", "3"]
isdecimalpresent = sequencestringnumbers[0].find(".")
print(isdecimalpresent) #print -1
print(isdecimalpresent >= 0) #print False
if isdecimalpresent >= 0:
    print([float(x) for x in sequencestringnumbers])
else:
    print([int(x) for x in sequencestringnumbers]) #print [1, 2, 3]


print("\n")
sequencestringnumbers = ["1", "2", "3"]
sequenceintegernumbers = [int(x) for x in sequencestringnumbers]
checkintegers = all(isinstance(x, int) for x in sequenceintegernumbers)
print(checkintegers) #print True
checkfloats = all(isinstance(x, float) for x in sequencestringnumbers)
print(checkfloats) #print False

print(isinstance("1", int)) #print False
print(isinstance(1, int)) #print True
print(isinstance(1.0, int)) #print False
print(isinstance(1.0, float)) #print True
print(isinstance(1.0, float)) #print True
