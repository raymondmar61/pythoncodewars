#https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
'''
Convert number to reversed array of digits 8kyu

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example (Input => Output):
35231 => [1,3,2,5,3]
0     => [0]
'''
def digitize(n):
    inputintegerstring = str(n)
    inputintegerstringlist = list(inputintegerstring)
    inputintegerstringlist.reverse()
    return list(map(int, inputintegerstringlist))


print(digitize(35231)) #print [1, 3, 2, 5, 3]
print(digitize(0)) #print [0]
print(digitize(23582357)) #print [7, 5, 3, 2, 8, 5, 3, 2]
print(digitize(984764738)) #print [8, 3, 7, 4, 6, 7, 4, 8, 9]
print(digitize(45762893920)) #print [0, 2, 9, 3, 9, 8, 2, 6, 7, 5, 4]
print(digitize(548702838394)) #print [4, 9, 3, 8, 3, 8, 2, 0, 7, 8, 4, 5]

inputinteger = 35231
inputintegerstring = str(inputinteger)
print(list(inputintegerstring)) #print ['3', '5', '2', '3', '1']
inputintegerstringlist = list(inputintegerstring)
inputintegerstringlist.reverse()
print(list(map(int, inputintegerstringlist))) #print [1, 3, 2, 5, 3]

#User submission
def digitize(n):
    return [int(x) for x in str(n)[::-1]]

def digitize(n):
    return [int(x) for x in reversed(str(n))]

def digitize(n):
    return map(int, reversed(str(n)))
