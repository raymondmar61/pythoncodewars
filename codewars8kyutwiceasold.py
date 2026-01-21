#https://www.codewars.com/kata/5b853229cfde412a470000d0/train/python
'''
Twice as old 8kyu

Your function takes two arguments:

current father's age (years)
current age of his son (years)

Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.
'''
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - (son_years_old * 2))


print(twice_as_old(36, 7)) #print 22
print(twice_as_old(55, 30)) #print 5
print(twice_as_old(42, 21)) #print 0
print(twice_as_old(22, 1)) #print 20
print(twice_as_old(29, 0)) #print 29


dad_years_old = 55
son_years_old = 30
son_years_olddouble = son_years_old * 2
print(son_years_olddouble) #print 60
print(dad_years_old) #print 55
print(dad_years_old - son_years_olddouble) #print -5
