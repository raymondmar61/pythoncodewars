#https://www.codewars.com/kata/57a5c31ce298a7e6b7000334/train/python
'''
Bin to Decimal 8 kyu

Complete the function which converts a binary number (given as a string) to a decimal number. #RM:  return float(inp, 2) returns error message.
'''
def bin_to_decimal(inp):
    return int(inp, 2)


print(bin_to_decimal("0")) #print 0
print(bin_to_decimal("1")) #print 1
print(bin_to_decimal("10")) #print 2
print(bin_to_decimal("11")) #print 3
print(bin_to_decimal("101010")) #print 42
print(bin_to_decimal("1001001")) #print 73
print(type(bin_to_decimal("1001001"))) #print <class 'int'>
