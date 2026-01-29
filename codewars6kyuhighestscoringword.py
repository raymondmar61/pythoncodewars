#https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
'''
Highest Scoring Word 6kyu

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''
def high(x):
    alphabetpoints = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
    xlist = x.split()
    bigtotal = 0
    highestscoringword = ""
    for eachxlist in xlist:
        total = 0
        for letter in eachxlist:
            total += alphabetpoints[letter]
        if total > bigtotal:
            bigtotal = total
            highestscoringword = eachxlist
    return highestscoringword


print(high("abad")) #print abad
print(high("man i need a taxi up to ubud")) #print taxi
print(high("what time are we climbing up the volcano")) #print volcano
print(high("take me to semynak")) #print semynak
print(high("aa b")) #print aa
print(high("b aa")) #print b
print(high("bb d")) #print bb
print(high("d bb")) #print d
print(high("aaa b")) #print aaa


alphabetpoints = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
print(alphabetpoints) #print {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
print(alphabetpoints["a"]) #print 1


sentence = "man i need a taxi up to ubud"
sentencelist = sentence.split()
print(sentencelist) #print ['man', 'i', 'need', 'a', 'taxi', 'up', 'to', 'ubud']
bigtotal = 0
highestscoringword = ""
for eachsentencelist in sentencelist:
    print(eachsentencelist) #print man
    total = 0
    for letter in eachsentencelist:
        print(letter) #print m
        print(alphabetpoints[letter]) #print 13
        total += alphabetpoints[letter]
    print(total) #print 28 RM:  13+1+14=28
    if total > bigtotal:
        bigtotal = total
        print("{} is the current highest score".format(eachsentencelist)) #print man is the current highest score
        highestscoringword = eachsentencelist
print("{} is the highest score word".format(highestscoringword)) #print taxi is the highest score word

#User submission
def high(x):
    words = x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]
