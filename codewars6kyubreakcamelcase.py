#https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
'''
Break camelCase 6kyu

Complete the solution so that the function will break up camel casing, using a space between words.

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

test.assert_equals(solution("helloWorld"), "hello World")
test.assert_equals(solution("camelCase"), "camel Case")
test.assert_equals(solution("breakCamelCase"), "break Camel Case")
'''
def solution(s):
    finalstring = ""
    for eachs in s:
        if eachs.isupper() == True:
            finalstring += " " + eachs.upper()
        else:
            finalstring += eachs
    return finalstring


print(solution("camelCasing"))
print(solution("identifier"))
print(solution(""))
print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))

originalstring = "breakCamelCase"
finalstring = ""
for eachoriginalstring in originalstring:
    if eachoriginalstring.isupper() == True:
        finalstring += " " + eachoriginalstring.upper()
    else:
        finalstring += eachoriginalstring
print(finalstring) #print break Camel Case

#Try using regular expressions
import re
originalstring = "breakCamelCase"
replace = re.compile(r"[A-Z]")
print(originalstring) #print breakCamelCase
print(replace.sub(r"", originalstring)) #print breakamelase
print(re.sub(r"[A-Z]", " ", originalstring)) #print break amel ase

#User solution regular expressions
import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)
