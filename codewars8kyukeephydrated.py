#https://www.codewars.com/kata/582cb0224e56e068d800003c/train/python
'''
Keep Hydrated! 8kyu

Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
'''
def litres(time):
    return int(time / 2)


print(litres(1.4)) #print 0
print(litres(12.3)) #print 6
print(litres(0.82)) #print 0
print(litres(11.8)) #print 5
print(litres(1787)) #print 893

timehours = 11.8
litresdrank = int(timehours / 2)
print(litresdrank) #print 5
