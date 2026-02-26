#https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/python
'''
Alternate capitalization 7 kyu

Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!

If you like this Kata, please try:

Indexed capitalization

Even-odd disparity
'''
def capitalize(s):
    slength = len(s)
    ssolution = ""
    for index in range(0, slength):
        if index % 2 == 0:
            ssolution += s[index].upper()
        else:
            ssolution += s[index]
    ssolutionswapcase = ssolution.swapcase()
    return [ssolution, ssolutionswapcase]


print(capitalize("abcdef")) #print ['AbCdEf', 'aBcDeF']
print(capitalize("codewars")) #print ['CoDeWaRs', 'cOdEwArS']
print(capitalize("abracadabra")) #print ['AbRaCaDaBrA', 'aBrAcAdAbRa']
print(capitalize("codewarriors")) #print ['CoDeWaRrIoRs', 'cOdEwArRiOrS']
print(capitalize("indexinglessons")) #print ['InDeXiNgLeSsOnS', 'iNdExInGlEsSoNs']
print(capitalize("codingisafunactivity")) #print ['CoDiNgIsAfUnAcTiViTy', 'cOdInGiSaFuNaCtIvItY']

#Using replace doesn't work because replace method replaces all the letters in a string
test = "abcdef"
print(test) #print abcdef
test = test.replace("c", "C")
print(test) #print abCdef

#User solution
def capitalize(s):
    s = ''.join(c if i % 2 else c.upper() for i, c in enumerate(s))
    return [s, s.swapcase()]

def capitalize(s):
    result = ['', '']
    for i, c in enumerate(s):
        result[0] += c.lower() if i % 2 else c.upper()
        result[1] += c.upper() if i % 2 else c.lower()
    return result
