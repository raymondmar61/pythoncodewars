#https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
'''
Get the Middle Character 7kyu

You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.

Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"
'''
def get_middle(s):
    stringlength = len(s)
    if stringlength % 2 == 0:
        indexnumber = (stringlength // 2) - 1
        return s[indexnumber:indexnumber + 2]
    else:
        indexnumber = (stringlength // 2)
        return s[indexnumber]


print(get_middle("test")) #print es
print(get_middle("testing")) #print t
print(get_middle("middle")) #print dd
print(get_middle("A")) #print A
print(get_middle("of")) #print of
