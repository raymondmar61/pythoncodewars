#https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python
'''
Remove First and Last Character Part Two 8 kyu

This is a spin off of my first kata http://www.codewars.com/kata/56bc28ad5bdaeb48760009b0

You are given a string containing a sequence of character sequences separated by commas.

Write a function which returns a new string containing the same character sequences except the first and the last ones but this time separated by spaces.

If the input string is empty or the removal of the first and last items would cause the resulting string to be empty, return an empty value (represented as a generic value NULL in the examples below).

Examples
"1,2,3"      =>  "2"
"1,2,3,4"    =>  "2 3"
"1,2,3,4,5"  =>  "2 3 4"

""     =>  None
"1"    =>  None
"1,2"  =>  None

RM:  The official solution was my submittal.
'''
def array(string):
    removefirstlastcharacter = string[2:-2]
    replacecommawithspace = str.maketrans(",", " ")
    checkempty = removefirstlastcharacter.translate(replacecommawithspace)
    if checkempty == "":
        return None
    else:
        return removefirstlastcharacter.translate(replacecommawithspace)


'''
print((array('1,2,3'))) #print 2
print((array('1,2,3,4'))) #print 2 3
print((array('1,2,3,4,5'))) #print 2 3 4
print((array(''))) #print None
print((array('1'))) #print None
print((array('1,2'))) #print None
'''

integerstring = '5 b6 '
removefirstlastcharacter = integerstring[1:-1]
print(removefirstlastcharacter) #print 2,3,4
if len(removefirstlastcharacter) == 0 or len(removefirstlastcharacter) == 1:
    print("None string length 0 or 1")
else:
    replacecommawithspace = str.maketrans(",", " ")
    print(removefirstlastcharacter.translate(replacecommawithspace)) #print 2 3 4

print(integerstring.split(",")) #print ['5 b6 ']
print(" ".join(integerstring.split(","))) #print 5 b6
print((" ".join(integerstring.split(",")))[1:-1]) #print  b6

print(integerstring.split(",")) #print ['5 b6 ']
print(integerstring.split(",")[1:-1]) #print []
print((integerstring.split(","))[1:-1]) #print []
print(" ".join(integerstring.split(",")[1:-1])) #print
print(" ".join(integerstring.split(","))[1:-1]) #print  b6
print("\n")

#Google AI.  Split the comma separated string into an array
#Split the comma-separated string into a list, remove the first and last items, and join the remaining elements with spaces. If the input is empty or contains fewer than three items, the function should return None.
def array(string):
    #Split by comma, slice off first and last, join with space, or return None if empty
    return ' '.join(string.split(',')[1:-1]) or None


print(array("1,2,3,4,5")) #return 2 3 4
print(array("5 b6 ")) #return None
print(array(" 31 c1 f32 b1 aeb ")) #return None


#https://cherono-mj.medium.com/remove-first-and-last-character-part-two-codewars-2d40d0090964
#Official solution from author's website
def array(string):
    separator_s = ' '
    results = separator_s.join(string.split(',')[1:-1])
    return results or None


print(array("1,2,3,4,5")) #return 2 3 4
print(array("5 b6 ")) #return None
print(array(" 31 c1 f32 b1 aeb ")) #return None