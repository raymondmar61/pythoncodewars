#https://www.codewars.com/kata/5761a717780f8950ce001473/train/python
'''
How old will I be in 2099? 8 kyu

Philip's just turned four and he wants to know how old he will be in various years in the future such as 2090 or 3044. His parents can't keep up calculating this so they've begged you to help them out by writing a programme that can answer Philip's endless questions.

Your task is to write a function that takes two parameters: the year of birth and the year to count years in relation to. As Philip is getting more curious every day he may soon want to know how many years it was until he would be born, so your function needs to work with both dates in the future and in the past.

Provide output in this format: For dates in the future: "You are ... year(s) old." For dates in the past: "You will be born in ... year(s)." If the year of birth equals the year requested return: "You were born this very year!"

"..." are to be replaced by the number, followed and proceeded by a single space. Mind that you need to account for both "year" and "years", depending on the result.

Good Luck!
'''
def calculate_age(year_of_birth, current_year):
    if current_year - year_of_birth == 1:
        return (f"You are 1 year old.")
    elif year_of_birth - current_year == 1:
        return (f"You will be born in 1 year.")
    elif current_year > year_of_birth:
        return (f"You are {current_year - year_of_birth} years old.")
    elif current_year < year_of_birth:
        return (f"You will be born in {year_of_birth - current_year} years.")
    elif current_year == year_of_birth:
        return (f"You were born this very year!")


print(calculate_age(2012, 2016)) #print "You are 4 years old."
print(calculate_age(1989, 2016)) #print "You are 27 years old."
print(calculate_age(2000, 2090)) #print "You are 90 years old."
print(calculate_age(2000, 1990)) #print "You will be born in 10 years."
print(calculate_age(2000, 2000)) #print "You were born this very year!"
print(calculate_age(900, 2900)) #print "You are 2000 years old."
print(calculate_age(2010, 1990)) #print "You will be born in 20 years."
print(calculate_age(2010, 1500)) #print "You will be born in 510 years."
print(calculate_age(2011, 2012)) #print "You are 1 year old."
print(calculate_age(2000, 1999)) #print "You will be born in 1 year."


year_of_birth = 2012
current_year = 2016
if current_year > year_of_birth:
    print(f"You are {current_year - year_of_birth} years old.") #print You are 4 years old.
elif current_year < year_of_birth:
    print(f"You will be born in {year_of_birth - current_year} years.")
elif current_year == year_of_birth:
    print(f"You were born this very year!")

#User submission
def calculate_age(year_of_birth, current_year):
    diff = abs(current_year - year_of_birth)
    plural = '' if diff == 1 else 's'
    if year_of_birth < current_year:
        return 'You are {} year{} old.'.format(diff, plural)
    elif year_of_birth > current_year:
        return 'You will be born in {} year{}.'.format(diff, plural)
    return 'You were born this very year!'

def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age == 0:
        return "You were born this very year!"
    elif age > 0:
        return "You are {} year{} old.".format(age, 's' if age > 1 else '')
    else:
        return "You will be born in {} year{}.".format(abs(age), 's' if abs(age) > 1 else '')
