#https://www.codewars.com/kata/57e1e61ba396b3727c000251/train/python
'''
String cleaning 8 kyu

Your boss decided to save money by purchasing some cut-rate optical character recognition software for scanning in the text of old novels to your database. At first it seems to capture words okay, but you quickly notice that it throws in a lot of numbers at random places in the text.

Examples (input -> output)
'! !'                 -> '! !'
'123456789'           -> ''
'This looks5 grea8t!' -> 'This looks great!'

Your harried co-workers are looking to you for a solution to take this garbled text and remove all of the numbers. Your program will take in a string and clean out all numeric characters, and return a string with spacing and special characters ~#$%^&!@*():;"'.,? all intact.
'''
def string_clean(s):
    finalstring = ""
    for eachs in s:
        if eachs.isnumeric():
            pass
        else:
            finalstring += eachs
    return finalstring


print(string_clean("! !")) #print ! !
print(string_clean("123456789")) #print
print(string_clean("(E3at m2e2!!)")) #print (Eat me!!)
print(string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!")) #print Dsa cdsc csa!!! I Am cool!
print(string_clean("A1 A1! AAA   3J4K5L@!!!")) #print A A! AAA   JKL@!!!
print(string_clean("Adgre2321 A1sad! A2A3A4 fv3fdv3J544K5L@")) #print Adgre Asad! AAA fvfdvJKL@
print(string_clean("Ad2dsad3ds21 A  1$$s122ad! A2A3Ae24 f44K5L@222222 ")) #print Addsadds A  $$sad! AAAe fKL@
print(string_clean("33333Ad2dsad3ds21 A3333  1$$s122a!d! A2!A!3Ae$24 f2##222 ")) #print Addsadds A  $$sa!d! A!A!Aef##
print(string_clean("My \"me3ssy\" d8ata issues2! Will1 th4ey ever, e3ver be3 so0lved?")) #print My \"messy\" data issues! Will they ever, ever be solved?
print(string_clean("Wh7y can't we3 bu1y the goo0d software3? #cheapskates3")) #print Why can't we buy the good software? #cheapskates

test = "This looks5 grea8t!"
replacenumbers = str.maketrans("1234567890", "          ")
print(test.translate(replacenumbers)) #print This looks  grea t!

finalstring = ""
for eachcharacter in test:
    print(eachcharacter)
    if eachcharacter.isnumeric():
        pass
    else:
        finalstring += eachcharacter
print(finalstring)
'''
T
h
i
s
 
l
o
o
k
s
5
 
g
r
e
a
8
t
!
This looks great!
'''

#User solution
def string_clean(s):
    return ''.join(x for x in s if not x.isdigit())
