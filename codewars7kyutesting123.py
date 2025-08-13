#https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python
'''
Testing 1-2-3 7kyu

Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.  RM:  can't use dictionary because the line numbering is part of the string.

Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
'''
def number(lines):
    newlist = []
    listofstringslen = len(lines)
    if listofstringslen == 0:
        return newlist
    else:
        for linenumber in range(1, listofstringslen + 1):
            newlist.append(f"{linenumber}: " + lines[linenumber - 1])
    return newlist


print(number([]))
print(number(["a", "b", "c"]))
print(number(["Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod", "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam", "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo", "consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse", "cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non", "proident, sunt in culpa qui officia deserunt mollit anim id est laborum."]))

listofstrings = ["Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod", "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam", "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo", "consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse", "cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non", "proident, sunt in culpa qui officia deserunt mollit anim id est laborum."]
listofstringslen = len(listofstrings)
print(listofstringslen) #print 6
if listofstringslen == 0:
    print(listofstrings)
else:
    for linenumber in range(1, listofstringslen + 1):
        print(f"{linenumber}: " + listofstrings[linenumber - 1]) #print 1: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod

for index, value in list(enumerate(listofstrings)):
    print(f"{index+1}: {value}") #print 1: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod

listcomprehension3 = [f"{index+1}: {value}" for index, value in list(enumerate(listofstrings)) if listofstrings]
print(listcomprehension3) #print ['1: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod', '2: tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam', '3: quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo', '4: consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse', '5: cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non', '6: proident, sunt in culpa qui officia deserunt mollit anim id est laborum.']

#RM:  I submitted the number2 function as return [f"{index+1}: {value}" for index, value in list(enumerate(lines)) if lines].  Top solutions used enumerate and list comprehension
def number2(lines):
    newlist = [f"{index+1}: {value}" for index, value in list(enumerate(lines)) if lines]
    return newlist


print(number2([]))
print(number2(["a", "b", "c"]))
print(number2(["Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod", "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam", "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo", "consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse", "cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non", "proident, sunt in culpa qui officia deserunt mollit anim id est laborum."]))
