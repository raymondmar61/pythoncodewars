#https://www.codewars.com/kata/57cff961eca260b71900008f/train/python
'''
Is there a vowel in there? 8 kyu

Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

If they are, change the array value to a string of that vowel.

input [100,100,116,105,117,121]=>[100,100,116,"i","u",121] output Return the resulting array.
'''
def is_vow(inp):
    inpfinal = []
    for eachinp in inp:
        if eachinp == 97:
            inpfinal.append("a")
        elif eachinp == 101:
            inpfinal.append("e")
        elif eachinp == 105:
            inpfinal.append("i")
        elif eachinp == 111:
            inpfinal.append("o")
        elif eachinp == 117:
            inpfinal.append("u")
        else:
            inpfinal.append(eachinp)
    return inpfinal


print(is_vow([118, 117, 120, 121, 117, 98, 122, 97, 120, 106, 104, 116, 113, 114, 113, 120, 106])) #print [118, "u", 120, 121, "u", 98, 122, "a", 120, 106, 104, 116, 113, 114, 113, 120, 106]
print(is_vow([101, 121, 110, 113, 113, 103, 121, 121, 101, 107, 103])) #print ["e", 121, 110, 113, 113, 103, 121, 121, "e", 107, 103]
print(is_vow([118, 103, 110, 109, 104, 106])) #print [118, 103, 110, 109, 104, 106]
print(is_vow([107, 99, 110, 107, 118, 106, 112, 102])) #print [107, 99, 110, 107, 118, 106, 112, 102]
print(is_vow([100, 100, 116, 105, 117, 121])) #print [100, 100, 116, "i", "u", 121]

print(ord("a")) #print 97
print(ord("e")) #print 101
print(ord("i")) #print 105
print(ord("o")) #print 111
print(ord("u")) #print 117

testcharactercodeslist = [100, 100, 116, 105, 117, 121]
testcharactercodeslistfinal = []
for eachtestcharactercodeslist in testcharactercodeslist:
    if eachtestcharactercodeslist == 97:
        testcharactercodeslistfinal.append("a")
    elif eachtestcharactercodeslist == 101:
        testcharactercodeslistfinal.append("e")
    elif eachtestcharactercodeslist == 105:
        testcharactercodeslistfinal.append("i")
    elif eachtestcharactercodeslist == 111:
        testcharactercodeslistfinal.append("o")
    elif eachtestcharactercodeslist == 117:
        testcharactercodeslistfinal.append("u")
    else:
        testcharactercodeslistfinal.append(eachtestcharactercodeslist)

print(testcharactercodeslistfinal) #print [100, 100, 116, 'i', 'u', 121]

#User solution
def is_vow(inp):
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]

def is_vow(inp):
    for i, v in enumerate(inp):
        if chr(v) in 'aeiou':
            inp[i] = chr(v)
    return inp

def is_vow(s):
    vowels = {97: 'a', 111: 'o', 117: 'u', 101: 'e', 105: 'i'}
    return [vowels.get(a, a) for a in s]
