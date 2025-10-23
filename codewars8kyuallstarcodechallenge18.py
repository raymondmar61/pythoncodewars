#https://www.codewars.com/kata/5865918c6b569962950002a1/train/python
'''
All Star Code Challenge #18 8kyu

Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

("Hello", 'o')  =>  1
("Hello", 'l')  =>  2
("", 'z')       =>  0

Notes
The first argument can be an empty string
In languages with no distinct character data type, the second argument will be a string of length 1
'''
def str_count(string, letter):
    count = 0
    for eachstring in string:
        if eachstring == letter:
            count += 1
    return count


print(str_count("hello", "l")) #print 2
print(str_count("hello", "e")) #print 1
print(str_count("codewars", "c")) #print 1
print(str_count("ggggg", "g")) #print 5
print(str_count("hello world", "o")) #print 2
print(str_count("", "z")) #print 0

word = "hello"
findcharacter = "l"
count = 0
for eachword in word:
    if eachword == findcharacter:
        count += 1
print(count) #print 2

'''
Top solution
def strCount(string, letter):
    return string.count(letter)
'''
