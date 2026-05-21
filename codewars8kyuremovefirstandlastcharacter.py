#https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python
'''
Remove First and Last Character 8 kyu

Remove First and Last Character
Task
Your goal is to write a function that removes the first and last characters of a string. You're given one parameter, the original string.

Important: Your function should handle strings of any length >= 2 characters. For strings with exactly 2 characters, return an empty string.

Examples
'eloquent' --> 'loquen'
'country'  --> 'ountr' 
'person'   --> 'erso'
'ab'       --> '' (empty string)
'xyz'      --> 'y'

Requirements
The input string will always have at least 2 characters
For strings with exactly 2 characters, return an empty string
For strings with 3 or more characters, remove the first and last character
The function should handle strings containing letters, numbers, and special characters

Test Cases
Your solution will be tested against:
Basic functionality with common words
Edge cases with 2-character and 3-character strings
Strings containing numbers and special characters
Random test cases of varying lengths
'''
def remove_char(s):
    if len(s) == 2:
        return ""
    elif len(s) == 3:
        return s[1]
    else:
        return s[1:-1]


print(remove_char('eloquent')) #print 'loquen'
print(remove_char('country')) #print 'ountr'
print(remove_char('person')) #print 'erso'
print(remove_char('place')) #print 'lac'
print(remove_char('ok')) #print ''
print(remove_char('ooopsss')) #print 'oopss'
print(remove_char('ab')) #print ''
print(remove_char('xyz')) #print 'y'


inputstring = "ab"
inputstring = "eloquent"
if len(inputstring) == 2:
    print("")
elif len(inputstring) == 3:
    print(inputstring[1])
else:
    print(inputstring[1:-1]) #print loquen

#User submission
def remove_char(s):
    return s[1: -1]
