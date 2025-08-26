#https://www.codewars.com/kata/559e708e72d342b0c900007b/train/python
'''
Even Odd Pattern #1 6kyu

Write a function that takes an array / list of numbers and returns a number.

See the examples and try to guess the pattern:

(1, 2, 6, 1, 6, 3, 1, 9, 6) => 393
(1, 2, 3)                   =>   5
(0, 2, 3)                   =>   3
(1, 0, 3)                   =>   3
(3, 2)                      =>   6

Google AI search result:  If the index of the number is even, add the number.  If the index of the number is odd, multiply the number.
'''
def even_odd(arr):
    answer = 0
    for counter in range(0, len(arr)):
        if counter % 2 == 0:
            answer += arr[counter]
        else:
            answer *= arr[counter]
    return answer


print(even_odd([1, 2, 6, 1, 6, 3, 1, 9, 6])) #print 396
print(even_odd([1, 2, 6, 1, 6, 1, 3, 9, 6])) #print 159
print(even_odd([1, 2, 2, 1, 6, 1, 3, 9, 6, 1])) #print 123
print(even_odd([1, 2, 3])) #print 5
print(even_odd([0, 2, 3])) #print 3
print(even_odd([1, 0, 3])) #print 3
print(even_odd([0, 0, 3])) #print 3
print(even_odd([3, 0])) #print 0
print(even_odd([1, 2, 2, 1, 6, 1, 3, 9, 6, 2, 32])) #print 278
print(even_odd([1, 2, 2, 1, 6, 10, 3, -1, 6, 2, 32])) #print -162

numberslist = [1, 2, 6, 1, 6, 3, 1, 9, 6]
answer = 0
for counter in range(0, len(numberslist)):
    if counter % 2 == 0:
        answer += numberslist[counter]
    else:
        answer *= numberslist[counter]
print(answer) #print 393

#Google AI
def even_odd_googleai(arr):
    answer = 0
    addnumber = True #Index 0 is even number.  First operation is add.
    for eachnumber in arr:
        if addnumber:
            answer += eachnumber
        else:
            answer *= eachnumber
        addnumber = not addnumber #Switch the operation or toggle between add and multiple
    return answer
