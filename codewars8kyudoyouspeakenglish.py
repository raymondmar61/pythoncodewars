#https://www.codewars.com/kata/58dbdccee5ee8fa2f9000058/train/python
'''
Do you speak "English"? 8 kyu

Given a string of arbitrary length with any ascii characters. Write a function to determine whether the string contains the whole word "English".

The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.

Upper or lower case letter does not matter -- "eNglisH" is also correct.

Return value as boolean values, true for the string to contains "English", false for it does not.
'''
def sp_eng(sentence):
    if sentence.lower().find("english") >= 0:
        return True
    else:
        return False


print(sp_eng("english")) #print True
print(sp_eng("egnlish")) #print False
print(sp_eng("engliish")) #print False
print(sp_eng("1234egn lis;h")) #print False
print(sp_eng("1234english ;k")) #print True
print(sp_eng("English")) #print True
print(sp_eng("eNgliSh")) #print True
print(sp_eng("1234#$%%eNglish ;k9")) #print True
print(sp_eng("EGNlihs")) #print False
print(sp_eng("1234englihs**")) #print False
print(sp_eng("")) #print False

givenstring = "abcEnglishdef"
print(givenstring.lower().find("english")) #print 3
givenstring = "abcnEglishsef"
print(givenstring.lower().find("english")) #print -1
givenstring = "english"
print(givenstring.lower().find("english")) #print 0
