#https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
'''
Detect Pangram

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabetlist = []
# for eachalphabet in alphabet:
#     alphabetlist.append(eachalphabet)
# print(alphabetlist)
# sentence = "The Quick Brown Fox Jumps Over The Lazy Dog"
# sentence = sentence.replace(" ", "")
# lowercase = sentence.lower()
# print(lowercase)
# for eachlowercase in lowercase:
#     print(eachlowercase)
#     if eachlowercase in alphabetlist:
#         alphabetlist.remove(eachlowercase)
#         print(alphabetlist)
#     if len(alphabetlist) == 0:
#         print("True")

def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetlist = []
    for eachalphabet in alphabet:
        alphabetlist.append(eachalphabet)
    st = st.replace(" ", "")
    lowercase = st.lower()
    for eachlowercase in lowercase:
        if eachlowercase in alphabetlist:
            alphabetlist.remove(eachlowercase)
    if len(alphabetlist) == 0:
        return True
    else:
        return False


sentence = "The Quick Brown Fox Jumps Over The Lazy Dog."
print(is_pangram(sentence)) #print True
sentence = "The Quick Brown Fox The Lazy Dog!"
print(is_pangram(sentence)) #print False
