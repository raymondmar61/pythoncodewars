#https://www.codewars.com/kata/unique-in-order
#6 Kyu earned
#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
def unique_in_order(teststring):
	uniquelist = []
	for n in range(0,len(teststring)):
		if n == 0:
			uniquelist.append(teststring[n])
		elif uniquelist[-1] == teststring[n]:
			pass
		else:
			uniquelist.append(teststring[n])
	print(uniquelist)

unique_in_order("AAAABBBCCDAABBB") #print ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order("ABBCcAD") #print ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3]) #print [1, 2, 3]






