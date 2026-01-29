#https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python
'''
Fix string case 7kyu

In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.

if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
'''
def solve(s):
    uppercounter = 0
    lowercounter = 0
    for eachs in s:
        if eachs.isupper():
            uppercounter += 1
        else:
            lowercounter += 1
    if uppercounter > lowercounter:
        return s.upper()
    else:
        return s.lower()


print(solve("code")) #print code
print(solve("CODe")) #print CODE
print(solve("COde")) #print code
print(solve("Code")) #print code

stringword = "coDe"
uppercounter = 0
lowercounter = 0
for eachstringword in stringword:
    if eachstringword.isupper():
        uppercounter += 1
    else:
        lowercounter += 1
print(uppercounter) #print 1
print(lowercounter) #print 3
if uppercounter > lowercounter:
    print(stringword.upper())
else:
    print(stringword.lower()) #print code
