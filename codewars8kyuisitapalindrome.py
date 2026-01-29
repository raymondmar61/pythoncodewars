#https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python
'''
Is it a palindrome? 8kyu

Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar.
'''
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]


print(is_palindrome('a')) #print True
print(is_palindrome('aba')) #print True
print(is_palindrome('Abba')) #print True
print(is_palindrome('malam')) #print True
print(is_palindrome('walter')) #print False
print(is_palindrome('kodok')) #print True
print(is_palindrome('Kasue')) #print False
print(is_palindrome('raymond2dnomyar')) #print True
print(is_palindrome('raym!onddno!myar')) #print True


print("racecar") #print racecar
print("racecar2"[::-1]) #print 2racecar
