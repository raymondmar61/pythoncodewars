#https://www.codewars.com/kata/53697be005f803751e0015aa/train/python
'''
The Vowel Code 6 kyu

Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.
'''
import string
def encode(st):
    return st.translate(str.maketrans("aeiou", "12345"))

def decode(st):
    return st.translate(str.maketrans("12345", "aeiou"))


print(encode('hello')) #print h2ll4
print(encode('How are you today?')) #print H4w 1r2 y45 t4d1y?
print(encode('This is an encoding test.')) #print Th3s 3s 1n 2nc4d3ng t2st.
print(decode('h2ll4')) #print hello

translateword = "hello"
print(translateword.translate(str.maketrans("aeiou", "12345"))) #print h2ll4.  aeiou is replaced with 12345 respectively.
untranslateword = "h2ll4"
print(untranslateword.translate(str.maketrans("12345", "aeiou"))) #print hello.  12345 is replaced with aeiou respectively.

replaceawithAewithEdeletex = str.maketrans("ae", "AE", "x") #character x is deleted
originalstring = "example string with some text"
print(originalstring) #print example string with some text
replacedstring = originalstring.translate(replaceawithAewithEdeletex)
print(replacedstring) #print EAmplE string with somE tEt
