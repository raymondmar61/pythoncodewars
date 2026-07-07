#https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
'''
Double Char 8 kyu

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
Good Luck!
'''
def double_char(s):
    repeatedstring = ""
    for eachs in s:
        repeatedstring += eachs * 2
    return repeatedstring


print(double_char("String")) #print SSttrriinngg
print(double_char("Hello World")) #print HHeelllloo  WWoorrlldd
print(double_char("1234!_ ")) #print 11223344!!__


givenstring = "String"
repeatedstring = ""
for eachgivenstring in givenstring:
    print(eachgivenstring * 2)
    repeatedstring += eachgivenstring * 2
print(repeatedstring)
'''
SS
tt
rr
ii
nn
gg
SSttrriinngg
'''

#User submission
def double_char(s):
    return ''.join(c * 2 for c in s)
