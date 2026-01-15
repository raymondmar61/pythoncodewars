#https://www.codewars.com/kata/57fae964d80daa229d000126/train/python
'''
Exclamation marks series #1: Remove an exclamation mark from the end of string 8kyu

Description:
Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.

Examples
"Hi!"     ---> "Hi"
"Hi!!!"   ---> "Hi!!"
"!Hi"     ---> "!Hi"
"!Hi!"    ---> "!Hi"
"Hi! Hi!" ---> "Hi! Hi"
"Hi"      ---> "Hi"
'''
def remove(s):
    if not s:
        return s
    elif s[-1] == "!":
        return s[:-1]
    else:
        return s


print(remove("Hi!")) #print Hi
print(remove("Hi!!!")) #print Hi!!
print(remove("!Hi")) #print !Hi
print(remove("!Hi!")) #print !Hi
print(remove("Hi! Hi!")) #print Hi! Hi
print(remove("Hi")) #print Hi
print(remove("")) #print

def removeassumenoemptystring(s):
    return s[:-1] if s[-1] == "!" else s


love = "Hi! Hi!"
print(love) #print Hi! Hi!
if love[-1] == "!":
    print(love[:-1]) #print Hi! Hi
else:
    print(love)

#User submission
def remove(s):
    return s[:-1] if s.endswith('!') else s
