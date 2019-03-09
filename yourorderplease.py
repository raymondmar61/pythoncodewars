#https://www.codewars.com/kata/your-order-please/train/python
#Kyu earned
#Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.  Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).  If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
#Examples:
#"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
#"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
#""  -->  ""

# def order(sentence):
#   # code here
#   return

#getnumber = "is2"
answer = []
getnumber = "is2 Thi1s T4est 3a"
print(getnumber)
getnumber.split(" ")
print(getnumber)
print(type(getnumber))
# for eachgetnumber in getnumber:
# 	print(eachgetnumber)
# getnumber = list(map(str,getnumber))
# print(getnumber)
# for eachgetnumber in getnumber:
# 	for eachgetnumber1 in eachgetnumber:
# 		if eachgetnumber1.isdigit() == True:
# 			answerindex = eachgetnumber1
# 			print(eachgetnumber1)
# 	answer.insert(answerindex,getnumber)
# print(answer)
	
testlistposition = []
testlistposition.insert(4,1400)
testlistposition.insert(5,500)
testlistposition.insert(0,94)
print(testlistposition) #print [94, 1400, 500]

letters = 'QH QD JC KD JS'
letters.split()
print(letters)

import re
string = 'This is a string, with words!'
re.findall(r'\w+', string)
print(string)
print(list(map(str,string))) #print [8, 4]