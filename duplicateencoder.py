#https://www.codewars.com/kata/duplicate-encoder
#6 Kyu earned.  Technically no Kyu earned.  Got solution another website.
"""
The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
RM:  one "("  two or more ")"
Examples:
"din" => "((("
"recede" => "()()()"
"Success" => ")())())"
"(( @" => "))(("
"""
from collections import Counter
def duplicateencoder(convertstring):
	convertstring = convertstring.lower()
	convertstringlist = list(convertstring)
	#print(Counter(convertstringlist))
	counterdictionary = Counter(convertstringlist)
	for key, value in counterdictionary.items():
		print(key, value)
		if (key == ")" and value == 1):
			convertstring = convertstring.replace(key,"(")
		elif (key == ")" and value >=2) or (key == "(" and value <= 1):
			print("I pass")
			pass
		elif value >= 2:
			convertstring = convertstring.replace(key,")")
		else:
			convertstring = convertstring.replace(key,"(")
		print(convertstring)
	return convertstring
# print(duplicateencoder("din")) #print (((
# print(duplicateencoder("recede")) #print ()()()
# print(duplicateencoder("Success")) #print )())())
# print(duplicateencoder("(( @")) #print ))((
print(duplicateencoder("dldwwTwe())")) #print )))))))))())))))(()())())(()(())()

# alist = ["a","b","c","d"]
# blist = "abzcdabzcd"
# blist = ["Z" if eachblist == "z" else eachblist for eachblist in blist]
# print(blist)

from collections import Counter
def duplicate_encode(word):
    word = word.lower()
    counter = Counter(word)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)