#https://www.codewars.com/kata/550498447451fbbd7600041c/train/python
'''
Are they the "same"? 6kyu

Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples
Valid arrays

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

Invalid arrays
If, for example, we change the first number to something else, comp is not returning true anymore:
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.

Remarks
a or b might be [] or {} (all languages except R, Shell).
a or b might be nil or null or None or nothing (except in C++, COBOL, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift).
If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.
'''

#https://www.youtube.com/watch?v=haZ_q4HYV4Y is correct.  Top solutions sorted the first array to match the second array.  No math calculations for the second array.
def comp(array1, array2):
    if type(array1) != list or type(array2) != list:
        return False
    result = []
    for eachinteger in array1:
        result.append(eachinteger**2)
    return sorted(result) == sorted(array2)


print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361])) #print True
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361])) #print False
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 36100, 25921, 361, 20736, 361])) #print False
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19])) #print False
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19])) #print False

#Function incorrect.  One incorrect result during the attempt.  Rest results are correct.
def comp(array1, array2):
    if type(array1) != list or type(array2) != list:
        return False
    numberofelements1 = len(array1)
    numberofelements2 = len(array2)
    for x in range(0, numberofelements1):
        array1[x] = abs(array1[x]) #convert negative numbers to positive numbers
        eacharray1square = array1[x]**2
        if eacharray1square not in array2:
            return False
    for x in range(0, numberofelements2):
        array2[x] = abs(array2[x]) #convert negative numbers to positive numbers
        eacharray2squareroot = array2[x]**(0.5)
        if eacharray2squareroot not in array1:
            return False
    return True


#Incorrect.  a[1]=2 and b[1]=9 is incorrect.  b[1] should be 4.  a[1]=2 and b[1]=4 is correct
a = [2, 2, 3]
b = [4, 9, 9]
numberofelements = len(a)
for x in range(0, numberofelements):
    print(a[x]) #print 2
    eachasquare = a[x]**2
    print(b[x]) #print 4
    eachbsquareroot = b[x]**(0.5)
    if (eachasquare in b) and (eachbsquareroot in a):
        print("true", eachasquare, eachbsquareroot) #print true 4 2.0
    else:
        print("false", a[x], eachasquare, b[x], eachbsquareroot)
        break

print(121**0.5) #print 11.0
print(132**0.5) #print 11.489125293076057
print(121**(1 / 2)) #print 11.0
print(132**(1 / 2)) #print 11.489125293076057

nothinglist = []
print(len(nothinglist)) #print 0

array1 = [121, 144, 19, 161, 19, 144, 19, 11]
array2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
if not array1 or not array2:
    print("I can't return False because the if statement is not a function")
if len(array1) == 0 or len(array2) == 0:
    print("I can't return False because the if statement is not a function")
print((121**0.5) == 11) #print True
print((132**0.5) == 11.489125293076057) #print True
print((121 ** (1 / 2)) == 11) #print True
print((132 ** (1 / 2)) == 11.489125293076057) #print True
