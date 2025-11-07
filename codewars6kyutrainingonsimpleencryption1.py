#https://www.codewars.com/kata/57814d79a56c88e3e0000786/python
'''
Training on Simple Encryption #1 - Alternating Split 6kyu

Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.
'''
def encrypt(text, n):
    integern = n
    if text == "":
        return text
    if integern <= 0:
        return text
    for counter in range(1, integern + 1):
        evenindexed = text[0::2]
        oddindexed = text[1::2]
        text = oddindexed + evenindexed
    return text


print(encrypt("012345", 1)) #print 135024
print(encrypt("012345", 2)) #print 304152
print(encrypt("012345", 3)) #print 012345
print(encrypt("01234", 1)) #print 13024
print(encrypt("01234", 2)) #print 32104
print(encrypt("01234", 3)) #print 20314
print(encrypt("", 3)) #print
print(encrypt("01234", -5)) #print 01234

def decrypt(encrypted_text, n):
    times = n
    if encrypted_text == "":
        return encrypted_text
    if times <= 0:
        return encrypted_text
    for xtimes in range(1, times + 1):
        starter = 0
        decryptstringlength = len(encrypted_text)
        decryptstringlengthstarter = decryptstringlength // 2
        stringdecrypted = ""
        #If the decryptstringlength is even numbered
        if decryptstringlength % 2 == 0:
            while decryptstringlengthstarter < decryptstringlength:
                stringdecrypted = stringdecrypted + encrypted_text[decryptstringlengthstarter] + encrypted_text[starter]
                starter += 1
                decryptstringlengthstarter += 1
        #Else the decryptstringlength is odd numbered
        else:
            while decryptstringlengthstarter < decryptstringlength:
                stringdecrypted = stringdecrypted + encrypted_text[decryptstringlengthstarter] + encrypted_text[starter]
                decryptstringlengthstarter += 1
                starter += 1
            stringdecrypted = stringdecrypted[:-1]
        encrypted_text = stringdecrypted
    return stringdecrypted


print(decrypt("hsi  etTi sats!", 1)) #print This is a test!
print(decrypt("s eT ashi tist!", 2)) #print This is a test!
print(decrypt(" Tah itse sits!", 3)) #print This is a test!
print(decrypt("This is a test!", 4)) #print This is a test!
print(decrypt("This is a test!", -1)) #print This is a test!

numberstring = "012345"
print(numberstring[0::2]) #print 024
print(numberstring[1::2]) #print 135
evenindexed = numberstring[0::2]
oddindexed = numberstring[1::2]
print(oddindexed + evenindexed) #print 135024
integern = 1
numberstring = "This is a test!"
if numberstring == "":
    print(numberstring)
if integern <= 0:
    print(numberstring)
for counter in range(1, integern + 1):
    evenindexed = numberstring[0::2]
    oddindexed = numberstring[1::2]
    numberstring = oddindexed + evenindexed
print(numberstring) #print hsi  etTi sats!

decrypt = "s eT ashi tist!"
decryptstringlength = len(decrypt)
starter = 0
decryptstringlengthstarter = decryptstringlength // 2
stringdecrypted = ""
times = 2
if decrypt == "":
    print(decrypt)
if times <= 0:
    print(decrypt)
for xtimes in range(1, times + 1):
    print("xtimes", xtimes)
    starter = 0
    decryptstringlengthstarter = decryptstringlength // 2
    stringdecrypted = ""
    if decryptstringlength % 2 == 0:
        print("even")
        while decryptstringlengthstarter < decryptstringlength:
            print(decryptstringlengthstarter, decrypt[decryptstringlengthstarter])
            print(starter, decrypt[starter])
            stringdecrypted = stringdecrypted + decrypt[decryptstringlengthstarter] + decrypt[starter]
            starter += 1
            decryptstringlengthstarter += 1
        print(stringdecrypted)
    else:
        print("odd")
        while decryptstringlengthstarter < decryptstringlength:
            print(decryptstringlengthstarter, decrypt[decryptstringlengthstarter])
            print(starter, decrypt[starter])
            stringdecrypted = stringdecrypted + decrypt[decryptstringlengthstarter] + decrypt[starter]
            decryptstringlengthstarter += 1
            starter += 1
        print(stringdecrypted[:-1])
        stringdecrypted = stringdecrypted[:-1]
    decrypt = stringdecrypted
    '''
    xtimes 1
    odd
    7 h
    0 s
    8 i
    1  
    9  
    2 e
    10 t
    3 T
    11 i
    4  
    12 s
    5 a
    13 t
    6 s
    14 !
    7 h
    hsi  etTi sats!
    xtimes 2
    odd
    7 T
    0 h
    8 i
    1 s
    9 
    ... 
    '''

#RM:  I didn't use the tuplelist in the if else while loop below.
decrypt = "s eT ashi tist!"
print(decrypt) #print s eT ashi tist!
print(len(decrypt)) #print 15
decryptstringlength = len(decrypt)
tuplelist = []
for number in range((decryptstringlength // 2), decryptstringlength):
    print(number, decrypt[number])
    print(tuple((number, decrypt[number])))
    tuplelist.append((number, decrypt[number]))
    '''
    7 h
    (7, 'h')
    8 i
    (8, 'i')
    9  
    (9, ' ')
    10 t
    (10, 't')
    11 i
    (11, 'i')
    '''
print("\n")
for counter in range(0, decryptstringlength // 2):
    print(counter, decrypt[counter])
    print(tuple((counter, decrypt[counter])))
    tuplelist.append((counter, decrypt[counter]))
    '''
    0 s
    (0, 's')
    1  
    (1, ' ')
    2 e
    (2, 'e')
    3 T
    (3, 'T')
    4  
    (4, ' ')
    5 a
    (5, 'a')
    '''
print(tuplelist) #print [(7, 'h'), (8, 'i'), (9, ' '), (10, 't'), (11, 'i'), (12, 's'), (13, 't'), (14, '!'), (0, 's'), (1, ' '), (2, 'e'), (3, 'T'), (4, ' '), (5, 'a'), (6, 's')]

#Top user submission
def decrypt(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text
