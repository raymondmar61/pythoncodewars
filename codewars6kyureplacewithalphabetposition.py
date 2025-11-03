#https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
'''
Replace With Alphabet Position 6kyu

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
'''

def alphabet_position(text):
    alphabetnumberposition = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
    output = ""
    for eachtext in text:
        eachtext = eachtext.lower()
        try:
            output = output + str(alphabetnumberposition[eachtext]) + " "
        except:
            continue
    return output.strip()


print(alphabet_position("The sunset sets at twelve o' clock.")) #print 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
print(alphabet_position("The narwhal bacons at midnight.")) #print 20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20


#Quick dictionary review
alphabetnumberposition = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
print(alphabetnumberposition["a"]) #print 1
getnumbers = "abc ABC"
output = ""
for eachgetnumbers in getnumbers:
    eachgetnumbers = eachgetnumbers.lower()
    try:
        print(eachgetnumbers, alphabetnumberposition[eachgetnumbers])
        '''
        a 1
        b 2
        c 3
        '''
        output = output + str(alphabetnumberposition[eachgetnumbers]) + " "
    except:
        continue
print(output) #print 1 2 3 1 2 3
