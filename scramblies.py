#https://www.codewars.com/kata/scramblies/train/python

"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
Only lower case letters will be used (a-z). No punctuation or digits will be included.

Input strings s1 and s2 are null terminated.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""

from itertools import permutations
from collections import Counter
def scramble(s1, s2):
	for eachs1 in s1:
		if eachs1 not in s2:
			return False
	print(s1, s2)
	print("Counters1",Counter(s1))
	print("Counters2",Counter(s2))
	news1 = []
	for eachs2 in s2:
		print(eachs2, news1.count(eachs2), s1.count(eachs2))
		if eachs2 not in s1:
			return False
		elif (news1.count(eachs2)) != (s1.count(eachs2)):
			news1.append(eachs2)
		print(eachs2, news1.count(eachs2), s1.count(eachs2))
		print("news1",news1)
	print("Counternews1",Counter(news1))
	if Counter(news1) != Counter(s2):
		return False
	scramblelist = []
	scramblelength = len(s2)	
	for x in permutations(news1,scramblelength):
		#print(x)
		x = ("".join(map(str, x)))
		if x not in scramblelist:
			scramblelist.append(x)
		if x == s2:
			return True
	return False

# s1 = "scriptjava"
# s2 = "javascript"
# for eachs2 in s2:
# 	if eachs2 not in s1:
# 		print(eachs2+" False")
# 	elif eachs2 in s1:
# 		print(eachs2+s1)


# def scramble(s1, s2):
# 	scramblelist = []
# 	scramblelength = len(s2)
# 	for x in permutations(s1,scramblelength):
# 		x = ("".join(map(str, x)))
# 		if x not in scramblelist:
# 			scramblelist.append(x)
# 	for eachscramblelist in scramblelist:
# 		if eachscramblelist == s2:			
# 			return True			
# 	return False
		
# colorlist1 = ["green","white","blue","blue","white","blue","green","white","green","yellow","white","blue","white","yellow","white","green","blue","red","red","white","blue","red","yellow","green","blue"]
# colorlist2 = ["green","white","blue","blue","white","blue","green","white","green","yellow","white","blue","white","yellow","white","green","blue","red","red","white","blue","red","yellow","green","blue"]
# counter1 = Counter(colorlist1)
# counter2 = Counter(colorlist2)
# print(counter1)
# print(counter2)
# print(counter1==counter2)


print(scramble("scriptjavx", "javascript")) #return False
print(scramble("javscripts", "javascript")) #return False
# print(scramble("rkqodlw", "world")) #return True
# print(scramble("cedewaraaossoqqyt", "codewars")) #return True
# print(scramble("katas", "steak")) #return False
# print(scramble("scriptjava", "javascript")) #return True
# print(scramble("scriptingjava", "javascript")) #return True

# for x in permutations("rkqodlw",5):
# 	x = ("".join(map(str, x)))
# 	#print(x)
# 	if x == "world":
# 		print("yes world")


