#https://www.codewars.com/kata/586c1cf4b98de0399300001d/train/python
'''
Grasshopper - Terminal game combat function 8 kyu

Create a combat function that takes the player's current health and the amount of damage received, and returns the player's new health. Health can't be less than 0.
'''
def combat(health, damage):
    newhealth = health - damage
    if newhealth <= 0:
        return 0
    else:
        return newhealth


print(combat(100, 5)) #print 95
print(combat(83, 16)) #print 67
print(combat(20, 30)) #print 0
