#https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python
'''
Printer Errors 7kyu

In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from a to z.

Examples:
s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"
'''
import re
def printer_error(s):
    countcorrectcolorletters = re.compile(r"[a-m]")
    numbercorrect = len(countcorrectcolorletters.findall(s))
    countincorrectcolorletters = re.compile(r"[^a-m]")
    numberincorrect = len(countincorrectcolorletters.findall(s))
    return f"{numberincorrect}/{(numbercorrect + numberincorrect)}"


print(printer_error("aaabbbbhaijjjm")) #print 0/14
print(printer_error("aaaxbbbbyyhwawiwjjjwwm")) #print 8/22
print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")) #print 3/56
print(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")) #print 6/60
print(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu")) #print 11/65

printcolorstring = "aaaxbbbbyyhwawiwjjjwwm"
printcolorstringlength = len(printcolorstring)
print(printcolorstringlength) #print 22
checkcolorletters = re.compile(r"\w{printcolorstringlength}")
print(checkcolorletters) #print re.compile('\\w{printcolorstringlength}')
checkcolorletters = re.compile(r"[a-m]{22,}")
print(checkcolorletters.findall(printcolorstring)) #print ['']
countcorrectcolorletters = re.compile(r"[a-m]")
print(countcorrectcolorletters.findall(printcolorstring)) #print ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'h', 'a', 'i', 'j', 'j', 'j', 'm']
print(len(countcorrectcolorletters.findall(printcolorstring))) #print 14
countincorrectcolorletters = re.compile(r"[^a-m]")
print(countincorrectcolorletters.findall(printcolorstring)) #print ['x', 'y', 'y', 'w', 'w', 'w', 'w', 'w']
print(len(countincorrectcolorletters.findall(printcolorstring))) #print 8

#User submission
from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]", '', s)), len(s))

def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
