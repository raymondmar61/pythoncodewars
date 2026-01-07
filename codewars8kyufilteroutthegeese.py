#https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python
'''
Filter out the geese 8kyu

Write a function that takes a list of strings as an argument and returns a filtered list containing the same elements but with the 'geese' removed.

The geese are any strings in the following array, which is pre-populated in your solution:  ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

For example, if this array were passed as an argument:  ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]

Your function would return the following array:  ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]

The elements in the returned array should be in the same order as in the initial array passed to your function, albeit with the 'geese' removed. Note that all of the strings will be in the same case as those provided, and some elements may be repeated.

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
'''
def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    birdsnogeese = []
    for eachbirds in birds:
        if eachbirds in geese:
            pass
        else:
            birdsnogeese.append(eachbirds)
    return birdsnogeese


print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"])) #print ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
print(goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"])) #print ['Mallard', 'Barbary', 'Hook Bill', 'Blue Swedish', 'Crested']
print(goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"])) #print []

#User solution using list comprehension
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]
