#https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python
'''
Fake Binary 8 kyu

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
'''
def fake_bin(x):
    replace5belowith05andabovewith1 = str.maketrans("0123456789", "0000011111")
    return x.translate(replace5belowith05andabovewith1)


print(fake_bin("45385593107843568")) #print 01011110001100111
print(fake_bin("509321967506747")) #print 101000111101101
print(fake_bin("366058562030849490134388085")) #print 011011110000101010000011011
print(fake_bin("15889923")) #print 01111100
print(fake_bin("800857237867")) #print 100111001111

test = "24680"
replace5belowwith0 = str.maketrans("01234", "00000")
print(test.translate(replace5belowwith0)) #print 00680
replace5andabovewith1 = str.maketrans("56789", "11111")
print(test.translate(replace5andabovewith1)) #print 24110
replace5belowith05andabovewith1 = str.maketrans("0123456789", "0000011111")
print(test.translate(replace5belowith05andabovewith1)) #print 00110
