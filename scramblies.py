#https://www.codewars.com/kata/scramblies/train/python
#Execution Timed Out (12000 ms).  Our servers are configured to only allow a certain amount of time for your code to execute. In rare cases the server may be taking on too much work and simply wasn't able to run your code efficiently enough. Most of the time though this issue is caused by inefficient algorithms. If you see this error multiple times you should try to optimize your code further.
"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
Only lower case letters will be used (a-z). No punctuation or digits will be included.

Input strings s1 and s2 are null terminated.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""

def scramble(s1, s2):
	s2answerlist = []
	s1 = list(s1)
	for eachs2 in s2:
		if eachs2 not in s1:
			return False
		else:
			s2answerlist.append(eachs2)
			s1.remove(eachs2)
	if ("".join(s2answerlist)) == s2:
		return True
	else:
		return False

print(scramble("scriptjavx", "javascript")) #print False
print(scramble("javscripts", "javascript")) #print False
print(scramble("rkqodlw", "world")) #print True
print(scramble("cedewaraaossoqqyt", "codewars")) #print True
print(scramble("katas", "steak")) #print False
print(scramble("scriptjava", "javascript")) #print True
print(scramble("scriptingjava", "javascript")) #print True
print(scramble("wtwfnhwqyotjkiid", "iyikwdtjthnfqwow")) #print True
print(scramble("pjhzddjljbo", "zohdpjdljbj")) #print True
print(scramble("ngqpvbwdxkfxkvqh", "xwfwaibmkzbrzzcl")) #print False

#https://www.reddit.com/r/learnpython/comments/3lo6b5/scrambled_string_comparison/
#Subtract the letters Counter from the word Counter. If the difference is an empty Counter, the letters Counter has excessive letters (and counts), and the word can be made from some or all of the letters.
from collections import Counter
def scramble(s1, s2):
    letters = Counter(s1)
    word = Counter(s2)
    diff = word - letters
    return len(diff) == 0
print(scramble('rkqodlw', 'world')) #print True
print(scramble('cedewaraaossoqqyt', 'codewars')) #print True
print(scramble('katas', 'steak')) #print False
#RM:  time is 11333ms just below 12000ms

#unknown website
def scramble(s1,s2):
    return all(s1.count(x) >= s2.count(x) for x in set(s2))
#RM:  time is 10883ms just below 12000ms