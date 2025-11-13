#https://www.codewars.com/kata/577bd026df78c19bca0002c0/train/python
'''
Correct the mistakes of the character recognition software 8kyu

Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

S is misinterpreted as 5
O is misinterpreted as 0
I is misinterpreted as 1
The test cases contain numbers only by mistake.
'''
def correct(s):
    s = s.replace("5", "S")
    s = s.replace("0", "O")
    s = s.replace("1", "I")
    return s


print(correct("L0ND0N")) #print LONDON
print(correct("DUBL1N")) #print DUBLIN
print(correct("51NGAP0RE")) #print SINGAPORE
print(correct("BUDAPE5T")) #print BUDAPEST
print(correct("PAR15")) #print PARIS

findstring = ("51NGAP0RE")
print(findstring.replace("5", "S")) #print S1NGAP0RE
print(findstring.replace("0", "O")) #print 51NGAPORE
print(findstring.replace("1", "I")) #print 5INGAP0RE

#User submissions
def correct(string):
    return string.translate(str.maketrans("501", "SOI"))

def correct(string):
    return string.replace('1', 'I').replace('0', 'O').replace('5', 'S')
