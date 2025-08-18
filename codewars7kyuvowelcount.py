#https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
'''
VowelCount 7kyu

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''
def get_count(sentence):
    count = 0
    for eachsentence in sentence:
        if eachsentence == "a" or eachsentence == "e" or eachsentence == "i" or eachsentence == "o" or eachsentence == "u":
            count += 1
    return count


print(get_count("aeiou")) #print 5
print(get_count("y")) #print 0
print(get_count("bcdfghjklmnpqrstvwxz y")) #print 0
print(get_count("")) #print 0
print(get_count("abracadabra")) #print 5

#A best practice
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")


sentence = "aeiou"
count = 0
for eachsentence in sentence:
    print(eachsentence) #printa\n e\n i\n o\n u
    if eachsentence == "a" or eachsentence == "e" or eachsentence == "i" or eachsentence == "o" or eachsentence == "u":
        count += 1
print(count) #print 5
