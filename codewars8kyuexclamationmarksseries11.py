#https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed/train/python
'''
Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence 8kyu

Description:
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
"Hi!" --> "H!!"
"!Hi! Hi!" --> "!H!! H!!"
"aeiou" --> "!!!!!"
"ABCDE" --> "!BCD!"
'''
def replace_exclamation(st):
    translationtable = str.maketrans("aeiouAEIOU", "!!!!!!!!!!")
    return st.translate(translationtable)


print(replace_exclamation("Hi!")) #print H!!
print(replace_exclamation("!Hi! Hi!")) #print !H!! H!!
print(replace_exclamation("aeiou")) #print !!!!!
print(replace_exclamation("ABCDE")) #print !BCD!

stringexclamation = "ABCDE"
#Create a translationtable replacing a, e, i, o, u, A, E, I, O, U each with !
translationtable = str.maketrans("aeiouAEIOU", "!!!!!!!!!!") #maketrans() method creates a mapping where the lower case vowels and uppercase vowels are each replaced with !
print(stringexclamation.translate(translationtable)) #print !BCD!  translate() method applies the mapping translationtable variable to the string stringexclamation variable resulting in the transformed string

#User submission
import re

def replace_exclamation(s):
    return re.sub('[aeiouAEIOU]', '!', s)
