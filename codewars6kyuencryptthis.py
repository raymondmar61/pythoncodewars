#https://www.codewars.com/kata/5848565e273af816fb000449/train/python
'''
Encrypt this! 6 kyu

Acknowledgments:
I thank yvonne-liu for the idea and for the example tests :)

Description:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter must be converted to its ASCII code.
The second letter must be switched with the last letter RM:  swap the second letter and the last letter for each word.
Keepin' it simple: There are no special characters in the input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
'''
def encrypt_this(text):
    textlist = text.split()
    encryptedtext = ""
    for eachtextlist in textlist:
        if len(eachtextlist) == 1:
            encryptedtext += str(ord(eachtextlist)) + " "
        elif len(eachtextlist) == 2:
            firstletterascii = str(ord(eachtextlist[0]))
            lastletter = eachtextlist[-1]
            encryptedtext += firstletterascii + lastletter + " "
        else:
            firstletterascii = str(ord(eachtextlist[0]))
            secondletter = eachtextlist[1]
            lastletter = eachtextlist[-1]

            encryptedtext += firstletterascii + lastletter + eachtextlist[2:-1] + secondletter + " "
    return encryptedtext[:-1]


print(encrypt_this("")) #print ""
print(encrypt_this("A wise old owl lived in an oak")) #print "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"
print(encrypt_this("The more he saw the less he spoke")) #print "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"
print(encrypt_this("The less he spoke the more he heard")) #print "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"
print(encrypt_this("Why can we not all be like that wise old bird")) #print "87yh 99na 119e 110to 97ll 98e 108ek116tah 119esi 111dl 98dri"),
print(encrypt_this("Thank you Piotr for all your help")) #print "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"

originalstring = "A wise old owl lived in an oak"
originalstringlist = originalstring.split()
print(originalstringlist)   #print ['A', 'wise', 'old', 'owl', 'lived', 'in', 'an', 'oak']
encryptedstring = ""
for eachoriginalstringlist in originalstringlist:
    print(eachoriginalstringlist)
    if len(eachoriginalstringlist) == 1:
        encryptedstring += str(ord(eachoriginalstringlist)) + " "
    elif len(eachoriginalstringlist) == 2:
        firstletterascii = str(ord(eachoriginalstringlist[0]))
        lastletter = eachoriginalstringlist[-1]
        encryptedstring += firstletterascii + lastletter + " "
    else:
        firstletterascii = str(ord(eachoriginalstringlist[0]))
        secondletter = eachoriginalstringlist[1]
        lastletter = eachoriginalstringlist[-1]
        print("first letter ascii " + firstletterascii)
        print("second letter " + secondletter)
        print("last letter " + lastletter)
        print(firstletterascii + lastletter + eachoriginalstringlist[2:-1] + secondletter)
        encryptedstring += firstletterascii + lastletter + eachoriginalstringlist[2:-1] + secondletter + " "
print(encryptedstring[:-1]) #print 65 119esi 111dl 111lw 108dvei 105n 97n 111ka
print(len(encryptedstring[:-1])) #print 44

originalstring = "Hello"
originalstring = "hello world"
originalstringlist = originalstring.split()
print(originalstringlist) #print ['hello', 'world']
encryptedstring = ""
for eachoriginalstringlist in originalstringlist:
    print(eachoriginalstringlist)
    firstletterascii = str(ord(eachoriginalstringlist[0]))
    secondletter = eachoriginalstringlist[1]
    lastletter = eachoriginalstringlist[-1]
    print("first letter ascii " + firstletterascii)
    print("second letter " + secondletter)
    print("last letter " + lastletter)
    print(firstletterascii + lastletter + eachoriginalstringlist[2:-1] + secondletter)

    encryptedstring += firstletterascii + lastletter + eachoriginalstringlist[2:-1] + secondletter + " "

    '''
    hello
    first letter ascii 104
    second letter e
    last letter o
    104olle
    hello
    world
    first letter ascii 119
    second letter o
    last letter d
    119drlo
    '''

print(encryptedstring[:-1]) #print 104olle 119drlo
print(len(encryptedstring[:-1])) #print 15

word = "the quick brown fox jumps over the lazy dog"
print(word) #print the quick brown fox jumps over the lazy dog
word = word.replace("brown", "blue")
print(word) #print the quick blue fox jumps over the lazy dog

#User solution
def swapper(w):
    return w if len(w) < 2 else w[-1] + w[1:-1] + w[0]

def encrypt_this(s):
    return ' '.join(w if not w else str(ord(w[0])) + swapper(w[1:]) for w in s.split())
