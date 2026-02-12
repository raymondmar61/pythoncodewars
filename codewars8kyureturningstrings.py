#https://www.codewars.com/kata/55a70521798b14d4750000a4/train/python
'''
Returning Strings 8kyu

Create a function that accepts a parameter representing a name and returns the message: "Hello, <name> how are you doing today?".

[Make sure you type the exact thing I wrote or the program may not execute properly]
'''
def greet(name):
    return "Hello, {} how are you doing today?".format(name)


print(greet('Ryan')) #print Hello, Ryan how are you doing today?
print(greet('Shingles')) #print Hello, Shingles how are you doing today?

print("Hello, {} how are you doing today?".format("Feeling Not My Name Today")) #print Hello, Feeling Not My Name Today how are you doing today?
