#https://www.codewars.com/kata/57a0885cbb9944e24c00008e/train/python
'''
Remove exclamation marks 8kyu

Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
'''
def remove_exclamation_marks(s):
    return s.replace("!", "")


teststring = "Hello!World! Hello!!World"
print(teststring.replace("!", "")) #print HelloWorld HelloWorld
