#https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python
'''
Will you make it? 8 kyu

You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

Considering these factors, write a function that tells you if it is possible to get to the pump or not.

Function should return true if it is possible and false if not.
'''
def zero_fuel(distance_to_pump, mpg, fuel_left):
    distanceremaining = mpg * fuel_left
    if distanceremaining >= distance_to_pump:
        return True
    else:
        return False


print(zero_fuel(50, 25, 2)) #print True
print(zero_fuel(100, 50, 1)) #print False

distance_to_pump = 50
mpg = 25
fuel_left = 2
distanceremaining = mpg * fuel_left
print(distanceremaining) #print 50
if distanceremaining >= distance_to_pump:
    print("True")
else:
    print("False")

distance_to_pump = 100
mpg = 50
fuel_left = 1
distanceremaining = mpg * fuel_left
print(distanceremaining) #print 50
if distanceremaining >= distance_to_pump:
    print("True")
else:
    print("False")
