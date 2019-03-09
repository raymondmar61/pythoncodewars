#https://www.codewars.com/kata/isograms/train/python
#7 Kyu earned
#An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
#is_isogram("Dermatoglyphics" ) == true
#is_isogram("aba" ) == false
#is_isogram("moOse" ) == false # -- ignore letter case
def is_isogram(string):
	checkedword = []
	if string == "":
		return True
	string = string.lower()
	for eachstring in string:	
		if eachstring not in checkedword:
			checkedword.append(eachstring)
		else:
			return False
	return True
print(is_isogram("Dermatoglyphics")) #print true
print(is_isogram("aba")) #print false
print(is_isogram("moOse")) #print false
