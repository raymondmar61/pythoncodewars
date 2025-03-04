#Code Wars 7kyu List Filtering
#https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/python
'''
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
'''
def filter_list(inputlist):
    integerslist = []
    for eachinput in inputlist:
        if isinstance(eachinput, int):
            integerslist.append(eachinput)
        else:
            pass
    return integerslist


positiveintegersstringslist = [1, 2, "a", "b"]
print(filter_list(positiveintegersstringslist)) #print [1, 2]
positiveintegersstringslist = [1, "a", "b", 0, 15]
print(filter_list(positiveintegersstringslist)) #print [1, 0, 15]
positiveintegersstringslist = [1, 2, "aasf", "1", "123", 123]
print(filter_list(positiveintegersstringslist)) #print [1, 2, 123]