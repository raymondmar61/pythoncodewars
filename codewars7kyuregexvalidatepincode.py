#https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
'''
Regex validate PIN code 7kyu

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
'''
import re
def validate_pin(pin):
    pinnumberregex = re.compile(r"\d\d\d\d$|\d\d\d\d\d\d$")
    # checkvalidpin = pinnumberregex.search(pin)
    checkvalidpin = re.fullmatch(pinnumberregex, pin)
    if checkvalidpin:
        return True
    else:
        return False


print(validate_pin("1234")) #print True
print(validate_pin("12345")) #print False
print(validate_pin("a234")) #print False
print(validate_pin("1")) #print False
print(validate_pin("12")) #print False
print(validate_pin("123")) #print False
print(validate_pin("12345")) #print False
print(validate_pin("1234567")) #print False
print(validate_pin("-1234")) #print False
print(validate_pin("-12345")) #print False
print(validate_pin("1.234")) #print False
print(validate_pin("00000000")) #print False
print(validate_pin("a234")) #print False
print(validate_pin(".234")) #print False
print(validate_pin("987654")) #print True
print(validate_pin("123456\n")) #print False

'''
\\d Any numeric digit from 0 to 9.
Use the dollar character after defining the character class.  Must end with dollar sign.
Pipe | is the or.
'''
pin = "123456"
# pinnumberregex = re.compile(r"\d\d\d\d$|\d\d\d\d\d\d$")
pinnumberregex = re.compile(r"(\d{4}|\d{6})$")
'''
fullmatch will only return a match object if the entire string matches the pattern. But since we don't have that function in the earlier versions, this behaviour can be simulated by adding a "$" at the end of our pattern. It shows that we want this pattern to only match the end of the string and match function matches the characters from the beginning only. So combining these properties, we get a pattern that will only match the entire string
'''
# checkvalidpin = pinnumberregex.search(pin)
print(re.fullmatch(pinnumberregex, pin)) #print <re.Match object; span=(0, 6), match='123456'>
checkvalidpin = re.fullmatch(pinnumberregex, pin)
print(checkvalidpin) #print <re.Match object; span=(0, 6), match='123456'>
try:
    print(checkvalidpin[0]) #print 123456
    print("True") #print True
except:
    print("False")
if checkvalidpin:
    print("True") #print True
else:
    print("False")

#No RegEx
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()