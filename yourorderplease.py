#https://www.codewars.com/kata/your-order-please/train/python
#6 Kyu earned
#Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.  Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).  If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
#Examples:
#"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
#"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
#""  -->  ""

def order(sentence):
	sentence = sentence.split(" ")
	answer = []
	answerindex = 0
	answerdictionary = {}
	for eachsentence in sentence:
		for eachsentencenumberindex in eachsentence:
			if eachsentencenumberindex.isdigit() == True:
				answerindex = int(eachsentencenumberindex)
				break
		answerdictionary[answerindex] = eachsentence
	for key, values in sorted(answerdictionary.items()):
		answer.insert(key,values)
	return " ".join(answer)
print(order("is2 Thi1s T4est 3a")) #print Thi1s is2 3a T4est
print(order("4of Fo1r pe6ople g3ood th5e the2")) #print Fo1r the2 g3ood 4of th5e pe6ople

#user solutions
# def order(sentence):
#     return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

# def order(sentence):
#   return " ".join(sorted(sentence.split(), key=min))

# def order(sentence):
#     return ' '.join(sorted(sentence.split(), key=sorted))