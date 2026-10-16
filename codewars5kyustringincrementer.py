#https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
'''
String incrementer 5 kyu

Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
'''
import re
def increment_string(string):
    if string == "":
        return "1"
    elif string[-1].isnumeric() is False:
        return string + "1"
    else:
        #Extract the number at the end
        extractnumberatend = re.findall(r"\d+$", string)
        extractfullinteger = "".join(extractnumberatend)
        extractnumberatendindexnumber = string.rindex(extractfullinteger)
        #Add one to extracted number at end as integer
        width = len(extractfullinteger)
        addonenumber = int(extractfullinteger) + 1
        addonenumberwithleadingzeros = f"{addonenumber:0{width}d}" #f-string
        #Replace number at end by inserting the number plus one at end
        return string[0:extractnumberatendindexnumber] + addonenumberwithleadingzeros


print(increment_string("foobar23")) #print foobar24
print(increment_string("foo0042")) #print foo0043
print(increment_string("foo9")) #print foo10
print(increment_string("foo")) #print foo1
print(increment_string("foobar001")) #print foobar002
print(increment_string("foobar1")) #print foobar2
print(increment_string("foobar00")) #print foobar01
print(increment_string("foobar99")) #print foobar100
print(increment_string("foobar099")) #print foobar100
print(increment_string("fo99obar99")) #print fo99obar100
print(increment_string("")) #print 1
print("\n")

import re
stringfoo = "foo00"
stringfoo = "foo089bar00098"
#Extract number at end as integer with leading zeros
extractnumberatend = re.findall(r"\d+$", stringfoo)
print(extractnumberatend) #print ['00098']
extractfullinteger = "".join(extractnumberatend)
print(extractfullinteger) #print 00098
extractnumberatendindexnumber = stringfoo.rindex(extractfullinteger)
print(extractnumberatendindexnumber) #print 9
#Add one to extracted number at end as integer using f-strings
width = len(extractfullinteger)
print(width) #print 5
addonenumber = int(extractfullinteger) + 1
addonenumberwithleadingzeros = f"{addonenumber:0{width}d}"
print(addonenumberwithleadingzeros) #print 00099
#Replace number at end by inserting the number plus one at end
print(stringfoo[0:extractnumberatendindexnumber] + addonenumberwithleadingzeros)

'''
#Extract number at end as integer with leading zeros
extractnumberatenddollarsign = re.compile(r"\d+$")
extractnumberatend = extractnumberatenddollarsign.findall(stringfoo)
print(extractnumberatend) #print ['00098']
extractfullinteger = "".join(extractnumberatend)
print(extractfullinteger) #print 00098
print(type(extractfullinteger)) #print <class 'str'>
#Extract number at end as integer without leading zeros
listtostring = "".join(extractnumberatend)
removezerosenddollarsign = re.compile(r"[1-9]*.$")
removezeros = removezerosenddollarsign.findall(listtostring)
print(removezeros) #print ['98']
#Add one to extracted number at end as integer
convertstringtointeger = int("".join(removezeros))
print(convertstringtointeger) #print 98
addonetoendstring = convertstringtointeger + 1
print(addonetoendstring) #print 99
#Replace number at end with number at end plus one
addonetoendstringwithleadingzeros = extractfullinteger.replace(str(convertstringtointeger), str(addonetoendstring))
print(addonetoendstringwithleadingzeros)
print(stringfoo.replace(extractfullinteger, addonetoendstringwithleadingzeros))
'''

stringfoo = "foo089bar00098"
numbers = re.findall(r"\d+$", stringfoo)
print(numbers) #print ['00098']
print(stringfoo.rindex("".join(numbers))) #print 9
print(stringfoo[0:stringfoo.rindex("".join(numbers))] + "00099") #print foo089bar00099

rawnumber = "00098"
width = len(rawnumber)
print(width) #print 5
newnumber = int(rawnumber) + 1
print(newnumber) #print 99
#f string
print(f"{newnumber:0{width}d}") #print 00099
print(f"{newnumber:0{1}d}") #print 99
print(f"{newnumber:0{2}d}") #print 99
print(f"{newnumber:0{3}d}") #print 099
print(f"{newnumber:0{4}d}") #print 0099
print(f"{newnumber:0{5}d}") #print 00099

checknumber = "5"
print(checknumber.isnumeric()) #print True
checknumber = "o"
print(checknumber.isnumeric()) #print True

nonumber = "foo"
if nonumber[-1].isnumeric() is False:
    print(nonumber + "1") #print foo1
emptystring = ""
if emptystring == "":
    print("1") #print 1

#User solution
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "":
        return strng + "1"
    return head + str(int(tail) + 1).zfill(len(tail))

def increment_string(strng):
    # strip the decimals from the right
    stripped = strng.rstrip('1234567890')
    # get the part of strng that was stripped
    ints = strng[len(stripped):]
    if len(ints) == 0:
        return strng + '1'
    else:
        # find the length of ints
        length = len(ints)
        # add 1 to ints
        new_ints = 1 + int(ints)
        # pad new_ints with zeroes on the left
        new_ints = str(new_ints).zfill(length)
        return stripped + new_ints
