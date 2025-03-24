#Abbreviate A Two Word Name
#https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python
'''
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
'''

name = "Sam Harris"
splitname = name.split()
print(splitname) #print ['Sam','Harris']
print(splitname[0][0]) #print S
print(splitname[1][0]) #print H
firstinitial = splitname[0][0].upper()
secondinitial = splitname[1][0].upper()
print(firstinitial + "." + secondinitial) #print S.H


def abbrev_name(name):
    splitname = name.split()
    firstinitial = splitname[0][0].upper()
    secondinitial = splitname[1][0].upper()
    return firstinitial + "." + secondinitial


print(abbrev_name("Sam Harris"))
print(abbrev_name("patrick feeney"))
