#https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python
'''
Write Number in Expanded Form 6kyu

You will be given a number and you will need to return it as a string in Expanded Form. For example:

12 --> "10 + 2"
45 --> "40 + 5"
70304 --> "70000 + 300 + 4"

NOTE: All numbers will be whole numbers greater than 0.

test.assert_equals(expanded_form(42), '40 + 2');
'''
def expanded_form(num):
    givennumberstring = str(num)
    givennumberstringlength = len(givennumberstring)
    givennumberlist = [*givennumberstring]
    placementnumber = list(range(givennumberstringlength, 0, -1))
    numberexpandedform = ""
    for eachgivennumberstring, eachplacementnumber in zip(givennumberstring, placementnumber):
        if eachgivennumberstring != "0":
            zeroes = "0" * (eachplacementnumber - 1)
            eachgivennumberstring = eachgivennumberstring + zeroes + " + "
            numberexpandedform = numberexpandedform + eachgivennumberstring
    return numberexpandedform[:-3]


print(expanded_form(12)) #print 10 + 2
print(expanded_form(45)) #print 40 + 5
print(expanded_form(70304)) #print 70000 + 300 + 4
print(expanded_form(42)) #print 40 + 2

givennumber = 70304
givennumberstring = str(givennumber)
givennumberstringlength = len(givennumberstring)
givennumberlist = [*givennumberstring]
placementnumber = list(range(givennumberstringlength, 0, -1))
print(givennumberlist) #print ['7', '0', '3', '0', '4']
print(placementnumber) #print [5, 4, 3, 2, 1]
numberexpandedform = ""
for eachgivennumberstring, eachplacementnumber in zip(givennumberstring, placementnumber):
    print(eachgivennumberstring) #print 7
    if eachgivennumberstring != "0":
        zeroes = "0" * (eachplacementnumber - 1)
        print(eachgivennumberstring + zeroes) #print 70000
        eachgivennumberstring = eachgivennumberstring + zeroes + " + "
        numberexpandedform = numberexpandedform + eachgivennumberstring
    print(numberexpandedform[:-3]) #print 70000