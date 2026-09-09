#https://www.codewars.com/kata/539de388a540db7fec000642/train/python
'''
The Coupon Code 7 kyu

Story
Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date.
All dates will be passed as strings in this format: "MONTH DATE, YEAR".
For the correct code and the entered code to match, both their values and data types must be the same. This means that e.g. false and 0 are not the same, and neither are 123 and "123".

Examples:
("123", "123", "July 9, 2015", "July 9, 2015")  ===>  true
(0,  false,    "July 9, 2015", "July 9, 2015")  ===>  false
("123", "123", "July 9, 2015", "July 2, 2015")  ===>  false
'''
import datetime
def check_coupon(entered_code, correct_code, current_date: str, expiration_date: str) -> bool:
    if type(entered_code) != type(correct_code):
        return False
    if entered_code != correct_code:
        return False
    #Convert date as string to date as datetime
    actualcurrent_date = datetime.datetime.strptime(current_date, "%B %d, %Y")
    actualexpiration_date = datetime.datetime.strptime(expiration_date, "%B %d, %Y")
    if actualcurrent_date > actualexpiration_date:
        return False
    return True


print(check_coupon("123", "123", "July 9, 2015", "July 9, 2015")) #print True
print(check_coupon(0, False, "July 9, 2015", "July 9, 2015")) #print False
print(check_coupon("123", "123", "July 9, 2015", "July 2, 2015")) #print False
print("\n")
print(check_coupon('123', '123', 'September 5, 2014', 'October 1, 2014')) #print True
print(check_coupon('123a', '123', 'September 5, 2014', 'October 1, 2014')) #print False
print(check_coupon('12abcd3', '12abcd3', 'January 5, 2014', 'January 1, 2014')) #print False
print(check_coupon('123ablqc0', '123ablqc0', 'July 5, 2000', 'July 5, 2000')) #print True
print(check_coupon('abc', 'abc', 'November 8, 2013', 'November 5, 2014')) #print True
print(check_coupon(0, False, 'September 5, 2014', 'September 25, 2014')) #print False
print(check_coupon('0', False, 'September 5, 2014', 'September 25, 2014')) #print False
print(check_coupon('1', True, 'September 5, 2014', 'September 25, 2014')) #print False
print("\n")
print(check_coupon(1 + 1, '2', 'September 5, 2014', 'September 25, 2014')) #print False
print(check_coupon('a12v564', 'a12v564', 'March 5, 1998', 'March 25, 1998')) #print True
print(check_coupon('0a12bc64', '0a12bc64', 'March 6, 2005', 'March 5, 2006')) #print True
print(check_coupon(1, True, 'September 5, 2014', 'September 25, 2014')) #print False
print(check_coupon("blah", "blahblah"[:4], 'September 5, 2014', 'September 25, 2014')) #print True

enteredcode = "123"
correctcode = "123"
currentdate = "July 9, 2015"
expirationdate = "July 9, 2015"

if type(enteredcode) != type(correctcode):
    print("False")
if enteredcode != correctcode:
    print("False")
if currentdate != expirationdate:
    print("False")
