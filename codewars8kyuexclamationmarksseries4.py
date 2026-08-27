#https://www.codewars.com/kata/57faf12b21c84b5ba30001b0/train/python
'''
Exclamation marks series #4: Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string 8 kyu

Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.

Examples
"Hi!"     ---> "Hi!"
"Hi!!!"   ---> "Hi!"
"!Hi"     ---> "Hi!"
"!Hi!"    ---> "Hi!"
"Hi! Hi!" ---> "Hi Hi!"
"Hi"      ---> "Hi!"
'''
def remove(st):
    return st.replace("!", "")+"!"

print(remove("Hi!")) #print "Hi!"
print(remove("Hi!!!")) #print Hi!"
print(remove("!Hi")) #print "Hi!"
print(remove("!Hi!")) #print "Hi!"
print(remove("Hi! Hi!")) #print "Hi Hi!"
print(remove("Hi")) #print "Hi!"


word = "Hi!!!"
word = "Hi! Hi!"
print(word.replace("!", "")+"!") #print Hi Hi!