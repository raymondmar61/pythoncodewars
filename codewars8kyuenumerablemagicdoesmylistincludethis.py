#https://www.codewars.com/kata/545991b4cbae2a5fda000158/train/python
'''
Enumerable Magic - Does My List Include This? 8 kyu

Create a method that accepts a list and an item, and returns true if the item belongs to the list, otherwise false.
'''
def include(arr, item):
    if item in arr:
        return True
    else:
        return False


lst = [2, 11, 0, 5000]
print(include(lst, 100)) #print False
print(include(lst, 2)) #print True
print(include(lst, 11)) #print True
print(include(lst, "2")) #print False
print(include(lst, 0)) #print True
print(include([], 0)) #print False

acceptlist = ["red", "blue", "green", "orange", "yellow", "black", "white"]
searchitem = "white"
if searchitem in acceptlist:
    print("True") #print True

#User submission
def include(arr, item):
    return item in arr
