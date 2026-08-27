#https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python
'''
Find the vowels 7 kyu

We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).

So given a string "super", we should return a list of [2, 4].

Some examples:
Mmmm  => []
Super => [2,4]
Apple => [1,5]
YoMama -> [1,2,4,6]
NOTES
Vowels in this context refers to: a e i o u y (including upper case)
This is indexed from [1..n] (not zero indexed!)
'''
def vowel_indices(word):
    return [n + 1 for n in range(0, len(word)) if word[n].lower() in "aeiouy"]


print(vowel_indices("mmm")) #print []
print(vowel_indices("apple")) #print [1,5]
print(vowel_indices("123456")) #print []
print(vowel_indices("UNDISARMED")) #print [1,4,6,9]
print(vowel_indices("Mmmm")) #print []
print(vowel_indices("Super")) #print [2, 4]
print(vowel_indices("Apple")) #print [1, 5]
print(vowel_indices("YoMama")) #print [1, 2, 4, 6]

vowelindexone = []
word = "Super"
word = "YoMama"
for n in range(0, len(word)):
    if word[n].lower() in "aeiouy":
        vowelindexone.append(n + 1)
print(vowelindexone) #print [1, 2, 4, 6]

listcomprehension = [n + 1 for n in range(0, len(word)) if word[n].lower() in "aeiouy"]
print(listcomprehension) #print [1, 2, 4, 6]
