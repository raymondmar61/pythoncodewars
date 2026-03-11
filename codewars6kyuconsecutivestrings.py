#https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python
'''
Consecutive strings 6 kyu

You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Examples:
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm, "nothing" in Erlang).
'''
def longest_consec(strarr, k):
    totalentries = len(strarr)
    if totalentries == 0 or k > totalentries or k <= 0:
        return ""
    solutionlist = []
    longeststringlength = 0
    for n in range(0, totalentries):
        consecutivestrings = strarr[n:n + k]
        if len(consecutivestrings) < k:
            break
        concatenatedstrings = "".join(consecutivestrings)
        concatenatedstringslength = len(concatenatedstrings)
        if concatenatedstringslength > longeststringlength:
            solutionlist.append((concatenatedstrings, concatenatedstringslength))
            longeststringlength = concatenatedstringslength
    for eachsolutionlist in solutionlist:
        if eachsolutionlist[1] == longeststringlength:
            return eachsolutionlist[0]
            break


print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2)) #print folingtrashy
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2)) #print abigailtheta
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)) #print abigailtheta
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)) #print oocccffuucccjjjkkkjyyyeehh
print(longest_consec([], 3)) #print
print(longest_consec(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)) #print wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck
print(longest_consec(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2)) #print wlwsasphmxxowiaxujylentrklctozmymu
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2)) #print
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3)) #print ixoyx3452zzzzzzzzzzzz
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15)) #print
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0)) #print

strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
k = 2
totalentries = len(strarr)
# print(totalentries) #print 6
# print(strarr[0:2]) #print ['tree', 'foling']
# print(strarr[1:3]) #print ['foling', 'trashy']
# print(strarr[2:4]) #print ['trashy', 'blue']
# print(strarr[3:5]) #print ['blue', 'abcdef']
# print(strarr[4:6]) #print ['abcdef', 'uvwxyz']
# print(strarr[5:7]) #print ['uvwxyz']
solutionlist = []
longeststringlength = 0
for n in range(0, totalentries):
    print(n)
    print(strarr[n:n + k])
    if len(strarr[n:n + k]) < k:
        print("love break for loop")
        break
    print("".join(strarr[n:n + k]))
    print(len("".join(strarr[n:n + k])))
    '''
    0
    ['tree', 'foling']
    treefoling
    10
    1
    ['foling', 'trashy']
    folingtrashy
    12
    ...
    '''
    if len("".join(strarr[n:n + k])) > longeststringlength:
        longeststringlength = len("".join(strarr[n:n + k]))
        solutionlist.append(("".join(strarr[n:n + k]), len("".join(strarr[n:n + k]))))
print(longeststringlength)
print(solutionlist) #print [('treefoling', 10), ('folingtrashy', 12)]
for eachsolutionlist in solutionlist:
    print(eachsolutionlist)
    '''
    ('treefoling', 10)
    ('folingtrashy', 12)
    '''
    if eachsolutionlist[1] == longeststringlength:
        print(eachsolutionlist[0]) #print folingtrashy
        break

#User solution
def longest_consec(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index + k])
            if len(s) > len(result):
                result = s

    return result
