#https://www.codewars.com/kata/559ac78160f0be07c200005a/train/python
'''
Name Shuffler 8kyu

Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

"john McClane" --> "McClane john"
'''
def name_shuffler(str_):
    firstnamelastnamesplit = str_.split(" ")
    return (" ".join(firstnamelastnamesplit[::-1]))


print(name_shuffler("john McClane")) #print McClane john
print(name_shuffler("Mary jeggins")) #print jeggins Mary
print(name_shuffler("tom jerry")) #print jerry tom

firstnamelastname = "john McClane"
firstnamelastnamesplit = firstnamelastname.split(" ")
print(firstnamelastnamesplit) #print ['john', 'McClane']
lastnamefirstname = firstnamelastnamesplit[1] + " " + firstnamelastnamesplit[0]
print(lastnamefirstname) #print McClane john
print(" ".join(firstnamelastnamesplit[::-1])) #print McClane john
