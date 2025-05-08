#https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
'''
Reverse words

Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''
def reverse_words(text):
    wordlength = len(text)
    reverseword = []
    temphold = []
    for i in range(0, wordlength + 1):
        if i == wordlength:
            temphold = "".join(temphold)
            reverseword.append(temphold)
            break
        elif text[i] != " ":
            temphold.insert(0, text[i])
        elif text[i] == " ":
            temphold.insert(i, " ")
            temphold = "".join(temphold)
            reverseword.append(temphold)
            temphold = []
    return "".join(reverseword)


print(reverse_words("This is an example!")) #print sihT si na !elpmaxe
print(reverse_words("double  spaces")) #print elbuod  secaps

#Selected answers
def reverse_words2original(str):
    return ' '.join(s[::-1] for s in str.split(' '))


print(reverse_words2original("This is an example!")) #print sihT si na !elpmaxe
print(reverse_words2original("double  spaces")) #print elbuod  secaps
print("\n")
def reverse_words2(str):
    print(str.split(" ")) #print ['This', 'is', 'an', 'example!'].  print ['double', '', 'spaces']
    temphold = []
    for s in str.split(' '):
        print("s", s) #print s This.  print s double
        print(''.join(s[::-1])) #print sihT.  print elbuod
        temphold.append(''.join(s[::-1]))
    print(temphold) #print ['sihT', 'si', 'na', '!elpmaxe'].  print ['elbuod', '', 'secaps']
    return ' '.join(temphold)


print(reverse_words2("This is an example!")) #print sihT si na !elpmaxe
print(reverse_words2("double  spaces")) #print elbuod  secaps


def reverse_words3(str):
    newStr = []
    for i in str.split(' '):
        newStr.append(i[::-1])
    return ' '.join(newStr)

print(reverse_words2("This is an example!")) #print sihT si na !elpmaxe
print(reverse_words2("double  spaces")) #print elbuod  secaps
