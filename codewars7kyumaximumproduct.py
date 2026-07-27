#https://www.codewars.com/kata/5a4138acf28b82aa43000117/train/python
'''
Maximum Product 7 kyu

Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array. Note that the array size is at least 2 and consists a mixture of positive, negative integers and also zeroes.

Examples
[1, 2, 3] returns 6 because the maximum product is obtained from multiplying 
 
2
∗
3
=
6
 2∗3=6
[9, 5, 10, 2, 24, -1, -48] returns 50 because the maximum product is obtained from multiplying 
 
5
∗
10
=
50
 5∗10=50
[-23, 4, -5, 99, -27, 329, -2, 7, -921] returns -14 because the maximum product is obtained from multiplying 
 
−
2
∗
7
=
−
14
 −2∗7=−14
'''
def adjacent_element_product(array):
    arraylength = len(array)
    maximumproduct = array[0] * array[1]
    for i in range(0, arraylength):
        for j in range(i + 1, arraylength):
            adjacentproduct = array[i] * array[j]
            if adjacentproduct > maximumproduct:
                maximumproduct = adjacentproduct
            break
    return maximumproduct


print(adjacent_element_product([5, 8])) #print 40
print(adjacent_element_product([1, 2, 3])) #print 6
print(adjacent_element_product([1, 5, 10, 9])) #print 90
print(adjacent_element_product([4, 12, 3, 1, 5])) #print 48
print(adjacent_element_product([3, 6, -2, -5, 7, 3])) #print 21
print(adjacent_element_product([9, 5, 10, 2, 24, -1, -48])) #print 50
print(adjacent_element_product([5, 6, -4, 2, 3, 2, -23])) #print 30
print(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921])) #print -14
print(adjacent_element_product([5, 1, 2, 3, 1, 4])) #print 6
print(adjacent_element_product([1, 0, 1, 0, 1000])) #print 0
print(adjacent_element_product([1, 2, 3, 0])) #print 6

integersarray = [1, 2, 3]
integersarray = [-23, 4, -5, 99, -27, 329, -2, 7, -921]
integersarray = [9, 5, 10, 2, 24, -1, -48]
integersarraylength = len(integersarray)
maximumproduct = integersarray[0] * integersarray[1]
for i in range(0, integersarraylength):
    print("i", i)
    for j in range(i + 1, integersarraylength):
        print("j", j)
        adjacentproduct = integersarray[i] * integersarray[j]
        print(integersarray[i], integersarray[j], adjacentproduct)
        if adjacentproduct > maximumproduct:
            maximumproduct = adjacentproduct
            print("maximumproduct", maximumproduct) #print maximumproduct 50
        break

#User solution
def adjacent_element_product(array):
    return max(a * b for a, b in zip(array, array[1:]))
