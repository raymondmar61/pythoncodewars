#https://www.codewars.com/kata/5aff237c578a14752d0035ae/train/python
'''
Predict your age! 7 kyu

My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!

In honor of my grandfather's memory we will write a function using his formula!

Take a list of ages when each of your great-grandparent died.
Multiply each number by itself.
Add them all together.
Take the square root of the result.
Divide by two.
Example
predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
Note: the result should be rounded down to the nearest integer.

Some random tests might fail due to a bug in the JavaScript implementation. Simply resubmit if that happens to you.
'''
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    ageslist = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    addthemalltogether = 0
    for n in range(0, len(ageslist)):
        addthemalltogether += (ageslist[n] * ageslist[n])
    return int((addthemalltogether**0.5) / 2)


print(predict_age(65, 60, 75, 55, 60, 63, 64, 45)) #print 86

ageslist = [65, 60, 75, 55, 60, 63, 64, 45]
addthemalltogether = 0
for n in range(0, len(ageslist)):
    addthemalltogether += (ageslist[n] * ageslist[n])
print(addthemalltogether) #print 30165
print(addthemalltogether**0.5) #print 173.68074159215234
print((addthemalltogether**0.5) / 2) #print 86.84037079607617
print(int((addthemalltogether**0.5) / 2)) #print 86
