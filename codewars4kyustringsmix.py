#https://www.codewars.com/kata/5629db57620258aa9d000014/train/python
'''
Strings Mix 4 kyu
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.
s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
'''
from collections import Counter
def mix(s1, s2):
    #Count letters each for s1 and s2.  Output is a dictionary.
    countsplittextinput1 = Counter(s1)
    breakcount1 = countsplittextinput1.most_common()
    solution1 = ""
    solution1dictionary = {}
    for letter, counter in breakcount1:
        if letter.isalpha() and letter.islower():
            solution1dictionary[letter] = counter
    countsplittextinput2 = Counter(s2)
    breakcount2 = countsplittextinput2.most_common()
    solution2 = ""
    solution2dictionary = {}
    for letter, counter in breakcount2:
        if letter.isalpha() and letter.islower():
            solution2dictionary[letter] = counter
    #Extract unique letters between s1 and s2.  Output is a list.
    keysolution1dictionary = list(solution1dictionary.keys())
    keysolution2dictionary = list(solution2dictionary.keys())
    combinekeysolution = sorted(list(set(keysolution1dictionary + keysolution2dictionary)))
    finalsolutiontuplelist = []
    #Get the maximum count for each letter in s1 and s2.   Also get the equal = in s1 and s2.
    for eachlowercase in combinekeysolution:
        solution1count = 0
        solution2count = 0
        if eachlowercase in keysolution1dictionary:
            solution1count = solution1dictionary[eachlowercase]
            if solution1count > 1:
                solution1count = solution1count
        if eachlowercase in keysolution2dictionary:
            solution2count = solution2dictionary[eachlowercase]
            if solution2count > 1:
                solution2count = solution2count
        maxcount = max(solution1count, solution2count)
        if solution1count <= 1 and solution2count <= 1:
            pass
        elif solution1count == maxcount and solution2count == maxcount:
            appendtuple = (solution1count, eachlowercase, f"=:{eachlowercase*solution1count}")
            finalsolutiontuplelist.append(appendtuple)
        elif solution1count == maxcount:
            appendtuple = (solution1count, eachlowercase, f"1:{eachlowercase*solution1count}")
            finalsolutiontuplelist.append(appendtuple)
        elif solution2count == maxcount:
            appendtuple = (solution2count, eachlowercase, f"2:{eachlowercase*solution2count}")
            finalsolutiontuplelist.append(appendtuple)
    #Sort the list of tuples.  Output is a single string.
    finalsolutiontuplelist.sort(key=lambda x: (-x[0], x[2][0], x[1]))
    finalsolutionsubstring = ""
    for eachsolution in finalsolutiontuplelist:
        finalsolutionsubstring = finalsolutionsubstring + eachsolution[2] + "/"
    return finalsolutionsubstring[:-1]


print(mix("A aaaa bb c", "& aaa bbb c d")) #print 1:aaaa/2:bbb
print(mix("my&friend&Paul has heavy hats! &", "my friend John has many many friends &")) #print 2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss
print(mix("mmmmm m nnnnn y&friend&Paul has heavy hats! &", "my frie n d Joh n has ma n y ma n y frie n ds n&")) #print 1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss
print(mix("Are the kids at home? aaaaa fffff", "Yes they are here! aaaaa fffff")) #print =:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh
print(mix("Are they here", "yes, they are here")) #print 2:eeeee/2:yy/=:hh/=:rr
print(mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp")) #print 2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz
print(mix("looping is fun but dangerous", "less dangerous than coding")) #print 1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg
print(mix(" In many languages", " there's a pair of functions")) #print 1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt
print(mix("Lords of the Fallen", "gamekult")) #print 1:ee/1:ll/1:oo
print(mix("codewars", "codewars")) #print
print(mix("A generation must confront the looming ", "codewarrs")) #print 1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr

#User solutions
def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))

def mix(s1, s2):
    s = []
    lett = "abcdefghijklmnopqrstuvwxyz"
    for ch in lett:
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) >= 2:
            if val1 > val2:
                s.append("1:" + val1 * ch)
            elif val1 < val2:
                s.append("2:" + val2 * ch)
            else:
                s.append("=:" + val1 * ch)

    s.sort()
    s.sort(key=len, reverse=True)
    return "/".join(s)


from collections import Counter


def mix(s1, s2):
    res = []
    c1 = Counter([c for c in s1 if c.islower()])
    c2 = Counter([c for c in s2 if c.islower()])
    for c in c1 | c2:
        if c1[c] > 1 and c1[c] > c2[c]:
            res += ['1:' + c * c1[c]]
        if c2[c] > 1 and c2[c] > c1[c]:
            res += ['2:' + c * c2[c]]
        if c1[c] > 1 and c1[c] == c2[c]:
            res += ['=:' + c * c1[c]]
    return '/'.join(sorted(res, key=lambda a: [-len(a), a]))
