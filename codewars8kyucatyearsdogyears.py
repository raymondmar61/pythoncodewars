#https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python
'''
Cat years, Dog years 8kyu

I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:
humanYears >= 1
humanYears are whole numbers only

Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that

Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
'''
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return ([1, 15, 15])
    elif human_years == 2:
        return ([2, 24, 24])
    else:
        catYears = (4 * (human_years - 2)) + (15 + 9)
        dogYears = (5 * (human_years - 2)) + (15 + 9)
        agelist = [human_years, catYears, dogYears]
        return (agelist)


print(human_years_cat_years_dog_years(1)) #print [1, 15, 15]
print(human_years_cat_years_dog_years(2)) #print [2, 24, 24]
print(human_years_cat_years_dog_years(3)) #print [3, 28, 29]
print(human_years_cat_years_dog_years(5)) #print [5, 36, 39]
print(human_years_cat_years_dog_years(10)) #print [10, 56, 64]

human_Years = 10
for counter in range(1, human_Years + 1):
    print("counter", counter)
    if counter == 1:
        print([1, 15, 15])
    elif counter == 2:
        print([2, 24, 24])
        catYears = 24
        dogYears = 24
    else:
        catYears = catYears + 4
        dogYears = dogYears + 5
        agelist = [counter, catYears, dogYears]
        print(agelist)
    '''
    counter 1
    [1, 15, 15]
    counter 2
    [2, 24, 24]
    counter 3
    [3, 28, 29]
    counter 4
    [4, 32, 34]
    counter 5
    [5, 36, 39]
    counter 6
    [6, 40, 44]
    counter 7
    [7, 44, 49]
    counter 8
    [8, 48, 54]
    counter 9
    [9, 52, 59]
    counter 10
    [10, 56, 64]
    '''

yearsago = 5
humanYears = 1
catYears = 15
dogYears = 15
agelist = [humanYears, catYears, dogYears]
print(agelist) #print [1, 15, 15]
humanYears = humanYears + 1
catYears = 15 + 9
dogYears = 15 + 9
agelist = [humanYears, catYears, dogYears]
print(agelist) #print [2, 24, 24]
humanYears = humanYears + 1
catYears = catYears + 4
dogYears = dogYears + 5
agelist = [humanYears, catYears, dogYears]
print(agelist) #print [3, 28, 29]
