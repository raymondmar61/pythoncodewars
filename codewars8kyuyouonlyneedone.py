#https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python
'''
You only need one - Beginner 8kyu

You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

a can contain numbers or strings. x can be either.

Return print if the array contains the value, false if not.
'''
def check(seq, elem):
    try:
        seq.index(elem)
        return True
    except:
        return False


print(check([66, 101], 66)) #print True
print(check([78, 117, 110, 99, 104, 117, 107, 115], 8)) #print False
print(check([101, 45, 75, 105, 99, 107], 107)) #print True
print(check([80, 117, 115, 104, 45, 85, 112, 115], 45)) #print True
print(check(['t', 'e', 's', 't'], 'e')) #print True
print(check(["what", "a", "great", "kata"], "kat")) #print False
print(check([66, "codewars", 11, "alex loves pushups"], "alex loves pushups")) #print True
print(check(["come", "on", 110, "2500", 10, '!', 7, 15], "Come")) #print False
print(check(["when's", "the", "next", "Katathon?", 9, 7], "Katathon?")) #print True
print(check([8, 7, 5, "bored", "of", "writing", "tests", 115], 45)) #print False
print(check(["anyone", "want", "to", "hire", "me?"], "me?")) #print True

lookingfor = "a"
submittedlist = ["what", "a", "great", "kata"]

print(submittedlist.index(lookingfor)) #print 1

lookingfor = "azz"
submittedlist = ["what", "a", "great", "kata"]

#print(submittedlist.index(lookingfor)) #print ValueError: 'azz' is not in list
try:
    submittedlist.index(lookingfor)
    print("true")
except:
    print("false") #print false

#User submission
def check(seq, elem):
    return elem in seq
