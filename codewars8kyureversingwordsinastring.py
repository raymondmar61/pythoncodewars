#https://www.codewars.com/kata/57a55c8b72292d057b000594/train/python
'''
Reversing Words in a String  8kyu

You need to write a function that reverses the words in a given string. Words are always separated by a single space.

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

Example (Input --> Output)

"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"

Happy coding!
'''
def reverse(st):
    stringtolist = st.split()
    reversestringtolist = stringtolist[::-1]
    reverselisttostring = " ".join(reversestringtolist)
    return reverselisttostring


print(reverse('Hello World')) #print World Hello
print(reverse('Hi There.')) #print There. Hi
print(reverse('Hi     There.   ')) #print There. Hi

forwardword = "Hi There."
print(forwardword.split()) #print ['Hi', 'There.']
print(forwardword.split()[::-1]) #print ['There.', 'Hi']
print(" ".join(forwardword.split()[::-1])) #print There. Hi

#User submission
def reverse(st):
    return " ".join(st.split()[::-1])
