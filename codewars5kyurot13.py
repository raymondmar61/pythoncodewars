#https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
'''
Rot13 5kyu

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
'''
def rot13(message):
    shiftletters = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
    return message.translate(shiftletters)


print(rot13("test")) #print grfg
print(rot13("Test")) #print Grfg
print(rot13("aA bB zZ 1234 *!?%")) #print nN oO mM 1234 *!?%

shiftletters = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
originalmessage1 = "Test"
encodedmessage1 = originalmessage1.translate(shiftletters)
print(encodedmessage1) #print Grfg
originalmessage2 = "aA bB zZ 1234 *!?%"
encodedmessage2 = originalmessage2.translate(shiftletters)
print(encodedmessage2) #print nN oO mM 1234 *!?%