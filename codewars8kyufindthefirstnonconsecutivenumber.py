#https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python
'''
Find the first non-consecutive number 8 kyu

Your task is to find the first element of an array that is not consecutive.

By not consecutive we mean not exactly 1 larger than the previous element of the array.

E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.

If the whole array is consecutive then return null.

The array will always have at least 2 elements^1 and all elements will be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!

^1 Can you write a solution that will return null2 for both [] and [ x ] though? (This is an empty array and one with a single number and is not tested for, but you can write your own example test. )
'''

def first_non_consecutive(arr):
    counter = 0
    stopcounter = len(arr) - 1
    while counter < stopcounter:
        presentnumber = arr[counter]
        presentnumberoneahead = arr[counter + 1]
        checkconsecutive = abs(presentnumber - presentnumberoneahead)
        if checkconsecutive != 1:
            return presentnumberoneahead
            break
        counter += 1
    return None


print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8])) #print 6
print(first_non_consecutive([1, 2, 3, 4, 5, 6, 7, 8])) #print None
print(first_non_consecutive([4, 6, 7, 8, 9, 11])) #print 6
print(first_non_consecutive([4, 5, 6, 7, 8, 9, 11])) #print 11
print(first_non_consecutive([31, 32])) #print None
print(first_non_consecutive([-3, -2, 0, 1])) #print 0
print(first_non_consecutive([-5, -4, -3, -1])) #print -1

consecutivelist = [1, 2, 3, 4, 6, 7, 8]

#Does not work because number list index number can be out of range
# for n in range(0, len(consecutivelist)):
#     presentnumber = consecutivelist[n]
#     presentnumberonelarger = consecutivelist[n] + 1
#     print(presentnumber, presentnumberonelarger)
#     if consecutivelist[n + 1] != presentnumberonelarger:
#         print("Error", consecutivelist[n + 1])
#         break

consecutivelist = [31, 32]
consecutivelist = [-5, -4, -3, -1]
consecutivelist = [-3, -2, 0, 1]
counter = 0
stopcounter = len(consecutivelist) - 1
while counter < stopcounter:
    print("counter", counter) #print counter 0
    presentnumber = consecutivelist[counter]
    presentnumberoneahead = consecutivelist[counter + 1]
    print(presentnumber, presentnumberoneahead) #print -3 -2
    print(presentnumber - presentnumberoneahead) #print -1
    print(abs(presentnumber - presentnumberoneahead) == 1) #print True
    checkconsecutive = abs(presentnumber - presentnumberoneahead)
    if checkconsecutive != 1:
        print("first nonconsecutivenumber", presentnumberoneahead) #print first nonconsecutivenumber 0
        break
    # if presentnumberonelarger != consecutivelist[counter + 1]:
    # if abs(presentnumber - consecutivelist[counter + 1]) != 1:
    #     print("Error", consecutivelist[counter + 1])
    #     break
    # else:
    #     print("All consecutive")
    #     break
    counter += 1

#User solution
def first_non_consecutive(a):
    i = a[0]
    for e in a:
        if e != i:
            return e
        i += 1
    return None
