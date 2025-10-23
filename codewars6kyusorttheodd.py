#https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
'''
Sort the odd 6kyu

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
'''
def sort_array(source_array):
    source_arrayindex = list(range(0, len(source_array)))
    oddlist = []
    oddlistindex = []
    for eachsource_array in zip(source_array, source_arrayindex):
        if eachsource_array[0] % 2 != 0:
            oddlist.append(eachsource_array[0])
            oddlistindex.append(eachsource_array[1])
    oddlist.sort()
    for eachoddlist in zip(oddlist, oddlistindex):
        source_array[eachoddlist[1]] = eachoddlist[0]
    return source_array


print(sort_array([7, 1]))
print(sort_array([5, 8, 6, 3, 4]))
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

#A clever solution
def sort_array(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


testlist = [5, 8, 6, 3, 4]
testlistindex = list(range(0, len(testlist)))
oddlist = []
oddlistindex = []
print(testlist) #print [5, 8, 6, 3, 4]
print(testlistindex) #print [0, 1, 2, 3, 4]
for eachtestlist in zip(testlist, testlistindex):
    print(eachtestlist) #print (5, 0)
    print(eachtestlist[0], eachtestlist[1]) #print 5 0
    if eachtestlist[0] % 2 != 0:
        print("odd") #print odd
        oddlist.append(eachtestlist[0])
        oddlistindex.append(eachtestlist[1])

print(oddlist) #print [5, 3]
oddlist.sort()
print(oddlist) #print [3, 5]
print(oddlistindex) #print [0, 3]
for eachoddlist in zip(oddlist, oddlistindex):
    testlist[eachoddlist[1]] = eachoddlist[0]

print(testlist) #print [3, 8, 6, 5, 4]
