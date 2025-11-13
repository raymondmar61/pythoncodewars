#https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python
'''
Anagram Detection 7kyu

An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK"
'''
def is_anagram(test, original):
    lowercasetest = test.lower()
    lowercaseoriginal = original.lower()
    separateletterslisttest = [*lowercasetest]
    separateletterslistoriginal = [*lowercaseoriginal]
    separateletterslisttest.sort()
    separateletterslistoriginal.sort()
    return separateletterslistoriginal == separateletterslisttest


print(is_anagram("foefet", "toffee")) #print True
print(is_anagram("Buckethead", "DeathCubeK")) #print True
print(is_anagram("Twoo", "WooT")) #print True
print(is_anagram("dumble", "bumble")) #print False
print(is_anagram("ound", "round")) #print False
print(is_anagram("apple", "pale")) #print False

test = "Buckethead"
lowercasetest = test.lower()
separateletterslisttest = [*lowercasetest] #Separate letters as a list
print(separateletterslisttest) #print ['b', 'u', 'c', 'k', 'e', 't', 'h', 'e', 'a', 'd']
separateletterslisttest.sort() #Sort a list of words or letters must be a list format
print(separateletterslisttest) #print ['a', 'b', 'c', 'd', 'e', 'e', 'h', 'k', 't', 'u']
original = "DeathCubeK"
lowercaseoriginal = original.lower()
separateletterslistoriginal = [*lowercaseoriginal] #Separate letters as a list
print(separateletterslistoriginal) #print ['d', 'e', 'a', 't', 'h', 'c', 'u', 'b', 'e', 'k']
separateletterslistoriginal.sort() #Sort a list of words or letters must be a list format
print(separateletterslistoriginal) #print ['a', 'b', 'c', 'd', 'e', 'e', 'h', 'k', 't', 'u']
print(separateletterslistoriginal == separateletterslisttest) #print True

#User submitted
def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())
