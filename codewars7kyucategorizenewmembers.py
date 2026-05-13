#https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
'''
Categorize New Member 7 kyu

The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

Output
Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

Example
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
'''
def open_or_senior(data):
    outputlist = []
    for eachdata in data:
        if eachdata[0] >= 55 and eachdata[1] > 7:
            outputlist.append("Senior")
        else:
            outputlist.append("Open")
    return outputlist


print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)])) #print ['Open', 'Senior', 'Open', 'Senior']
print(open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)])) #print ['Open', 'Open', 'Senior', 'Open']

memberslist = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
outputlist = []
for eachmemberslist in memberslist:
    print(eachmemberslist) #print [18, 20]\n [45, 2]\n [61, 12]\n [37, 6]\n [21, 21]\n [78, 9]
    if eachmemberslist[0] >= 55 and eachmemberslist[1] > 7:
        outputlist.append("Senior")
    else:
        outputlist.append("Open")
print(outputlist) #print ['Open', 'Open', 'Senior', 'Open', 'Open', 'Senior']

#User submission
def openOrSenior(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
