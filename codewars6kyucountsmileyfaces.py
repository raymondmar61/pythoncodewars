#https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python
'''
Count the smiley faces! 6kyu

Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

countSmileys([':)', ';(', ';}', ':-D']);       // should return 2; :) and :-D
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3; ;D and :-) and ;~)
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1; ;-D

Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.
'''
def count_smileys(arr):
    count = 0
    for eachlist1 in arr:
        if eachlist1[0] == ";" or eachlist1[0] == ":":
            if eachlist1[1] == "-" or eachlist1[1] == "~":
                if eachlist1[2] == ")" or eachlist1[2] == "D":
                    count += 1
            if eachlist1[1] == ")" or eachlist1[1] == "D":
                count += 1
    return count


print(count_smileys([":)", ";(", ";}", ":-D"])) #print 2
print(count_smileys([";D", ":-(", ":-)", ";~)"])) #print 3
print(count_smileys([";]", ":[", ";*", ":$", ";-D"])) #print 1
print(count_smileys([])) #print 0


list1 = [':)', ';(', ';}', ':-D']
list1 = [';D', ':-(', ':-)', ';~)']
list1 = [';]', ':[', ';*', ':$', ';-D']
list1 = []
count = 0
for eachlist1 in list1:
    print(eachlist1)
    if eachlist1[0] == ";" or eachlist1[0] == ":":
        if eachlist1[1] == "-" or eachlist1[1] == "~":
            if eachlist1[2] == ")" or eachlist1[2] == "D":
                print("found smile 1" + eachlist1)
                count += 1
        if eachlist1[1] == ")" or eachlist1[1] == "D":
            print("found smile 2" + eachlist1)
            count += 1
print(count) #print 0
