#https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
'''
String ends with?

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''
def solution(text, ending):
    endinglength = len(ending)
    textending = text[-endinglength:]
    if textending == ending:
        return True
    else:
        return False


text = "abc"
ending = "bc"
endinglength = len(ending)
print(endinglength) #print 2
textending = text[-endinglength:]
print(textending) #print bc
if textending == ending:
    print(True) #print True
else:
    print(False)

text = "abc"
ending = "d"
endinglength = len(ending)
print(endinglength) #print 1
textending = text[-endinglength:]
print(textending) #print c
if textending == ending:
    print(True)
else:
    print(False) #print False

print(solution("abc", "bc")) #print True
print(solution("samurai", "ai")) #print True
print(solution("ninja", "ja")) #print True
print(solution("sensei", "i")) #print True
print(solution("abc", "abc")) #print True
print(solution("abcabc", "bc")) #print True
print(solution("fails", "ails")) #print True
print(solution("sumo", "omo")) #print False
print(solution("samurai", "ra")) #print False
print(solution("abc", "abcd")) #print False
print(solution("ails", "fails")) #print False
print(solution("this", "fails")) #print False
print(solution("spam", "eggs")) #print False
