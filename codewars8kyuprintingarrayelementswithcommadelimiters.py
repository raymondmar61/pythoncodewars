#https://www.codewars.com/kata/56e2f59fb2ed128081001328/train/python
'''
Printing Array elements with Comma delimiters 8 kyu

Input: Array of elements

["h","o","l","a"]

Output: String with comma delimited elements of the array in th same order.

"h,o,l,a"

Note: if this seems too simple for you try the next level

Note2: the input data can be: boolean array, array of objects, array of string arrays, array of number arrays...
'''
def print_array(arr):
    commadelimited = ""
    for eacharr in arr:
        commadelimited += str(eacharr) + ","
    return (commadelimited[:-1])


data = [2]
print(print_array(data)) #print 2

data = [2, 4, 5, 2]
print(print_array(data)) #print 2,4,5,2

data = [2, 4, 5, 2]
print(print_array(data)) #print 2,4,5,2

data = [2.0, 4.2, 5.1, 2.2]
print(print_array(data)) #print 2.0,4.2,5.1,2.2

data = ["2", "4", "5", "2"]
print(print_array(data)) #print 2,4,5,2

data = [True, False, False]
print(print_array(data)) #print True,False,False

array1 = ["hello", "this", "is", "an", "array!"]
array2 = ["a", "b", "c", "d", "e!"]
data = array1 + array2
print(print_array(data)) #print hello,this,is,an,array!,a,b,c,d,e!

array1 = ["hello", "this", "is", "an", "array!"]
array2 = [1, 2, 3, 4, 5]
data = [array1, array2]
print(print_array(data)) #print ['hello', 'this', 'is', 'an', 'array!'],[1, 2, 3, 4, 5]


dataarray = [2, 4, 5, 2]
commadelimited = ""
for eachdataarray in dataarray:
    commadelimited += str(eachdataarray) + ","
print(commadelimited[:-1]) #print 2,4,5,2
dataarray = ["2", "4", "5", "2"]
commadelimited = ""
for eachdataarray in dataarray:
    commadelimited += str(eachdataarray) + ","
print(commadelimited[:-1]) #print 2,4,5,2

array1 = ["hello", "this", "is", "an", "array!"]
array2 = [1, 2, 3, 4, 5]
dataarray = [array1, array2]
commadelimited = ""
for eachdataarray in dataarray:
    print(eachdataarray) #print ['hello', 'this', 'is', 'an', 'array!']\n [1, 2, 3, 4, 5]
    commadelimited += str(eachdataarray) + ","
print(commadelimited[:-1]) #print ['hello', 'this', 'is', 'an', 'array!'],[1, 2, 3, 4, 5]
print(type(commadelimited[:-1])) #print <class 'str'>

#User solution
def print_array(arr):
    return ','.join(map(str, arr))
