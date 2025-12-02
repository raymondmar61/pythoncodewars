#https://www.codewars.com/kata/568d0dd208ee69389d000016/train/python
'''
Transportation on vacation 8kyu

After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).
'''
def rental_car_cost(d):
    dailyrent = 40
    sevendaydiscount = 50
    threedaydiscount = 20
    totalrent = dailyrent * d
    if 3 <= d <= 6:
        return totalrent - threedaydiscount
    elif d >= 7:
        return totalrent - sevendaydiscount
    else:
        return totalrent


print(rental_car_cost(1)) #print 40
print(rental_car_cost(4)) #print 140
print(rental_car_cost(7)) #print 230
print(rental_car_cost(8)) #print 270


dailyrent = 40
sevendaydiscount = 50
threedaydiscount = 20
days = 8

totalrent = dailyrent * days
if 3 <= days <= 6:
    totalrent = totalrent - threedaydiscount
elif days >= 7:
    totalrent = totalrent - sevendaydiscount
print(totalrent) #print 270

#User submission
def rental_car_cost(d):
    return d * 40 - (d > 2) * 20 - (d > 6) * 30
