#https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
'''
Shortest Word 7kyu
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types
'''
def find_short(s):
    counterlist = []
    stringsamplelist = s.split()
    for eachstringsample in stringsamplelist:
        eachstringlength = (len(eachstringsample))
        counterlist.append(eachstringlength)
    return min(counterlist)


print(find_short("bitcoin take over the world maybe who knows perhaps")) #print 3
print(find_short("turns out random test cases are easier than writing out basic ones")) #print 3
print(find_short("lets talk about javascript the best language")) #print 3
print(find_short("i want to travel the world writing code one day")) #print 1
print(find_short("Lets all go on holiday somewhere very cold")) #print 2
print(find_short("Let's travel abroad shall we")) #print 2

stringsample = "bitcoin take over the world maybe who knows perhaps"

counterlist = []
stringsamplelist = stringsample.split()
for eachstringsample in stringsamplelist:
    print(eachstringsample) #print bitcoin
    print(len(eachstringsample)) #print 7
    eachstringlength = (len(eachstringsample))
    counterlist.append(eachstringlength)
print(min(counterlist)) #print 3

#best solution
def find_short(s):
    return min(len(x) for x in s.split())
