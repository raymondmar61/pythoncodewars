#Descending Order
#https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
#Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
#Examples:  Input: 42145 Output: 54421.  Input: 145263 Output: 654321.  Input: 123456789 Output: 987654321

inputnumber = 42145
inputnumber = str(inputnumber)
print(inputnumber) #print 42145
print(type(inputnumber)) #print <class 'str'>
inputsplit = list(map(str, inputnumber))
print(inputsplit) #print ['4', '2', '1', '4', '5']
inputsplit.sort(reverse=True)
print(inputsplit) #print ['5', '4', '4', '2', '1']
print("".join(inputsplit)) #print 54421
print(type("".join(inputsplit))) #print <class 'str'>
print(int("".join(inputsplit))) #print 54421
print(type(int("".join(inputsplit)))) #print <class 'int'>
print("\n")

def descending_order(num):
    inputnumber = str(num)
    inputsplit = list(map(str, inputnumber))
    inputsplit.sort(reverse=True)
    return int("".join(inputsplit))


print(descending_order(42145)) #print 54421
print(descending_order(145263)) #print 654321
print(descending_order(123456789)) #print 987654321
