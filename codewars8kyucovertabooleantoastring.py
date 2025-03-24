#Convert A Boolean To A String
#https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python
#Implement a function which convert the given boolean value into its string representation.
print(True) #print True
print(str(True)) #print True
print(type(str(True))) #print <class 'str'>

def boolean_to_string(b):
    b = str(b)
    return b


print(boolean_to_string(True)) #print True
print(boolean_to_string(False)) #print False
