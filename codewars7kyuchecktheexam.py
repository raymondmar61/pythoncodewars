#https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python
'''
Check the exam 7 kyu

The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"]. The second one contains a student's submitted answers.

The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer, represented as an empty string (in C the space character is used).

If the score < 0, return 0.

For example:

    Correct answer    |    Student's answer   |   Result         
 ---------------------|-----------------------|-----------
 ["a", "a", "b", "b"]   ["a", "c", "b", "d"]  →     6
 ["a", "a", "c", "b"]   ["a", "a", "b", "" ]  →     7
 ["a", "a", "b", "c"]   ["a", "a", "b", "c"]  →     16
 ["b", "c", "b", "a"]   ["" , "a", "a", "c"]  →     0
'''
def check_exam(arr1, arr2):
    score = 0
    for n in range(0, len(arr1)):
        if arr1[n] == arr2[n]:
            score += 4
        elif arr2[n] == "":
            score += 0
        elif arr1[n] != arr2[n]:
            score -= 1
    if score < 0:
        return 0
    else:
        return score


print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"])) #print 6
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b", ""])) #print 7
print(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"])) #print 16
print(check_exam(["b", "c", "b", "a"], ["", "a", "a", "c"])) #print 0

correctanswer = ["a", "a", "b", "b"]
studentanswer = ["a", "c", "b", "d"]
correctanswer = ["b", "c", "b", "a"]
studentanswer = ["", "a", "a", "c"]
correctanswer = ["a", "a", "c", "b"]
studentanswer = ["a", "a", "b", ""]

print(correctanswer[0], studentanswer[0]) #print a a
print(correctanswer[1], studentanswer[1]) #print a c
score = 0
for n in range(0, len(correctanswer)):
    if correctanswer[n] == studentanswer[n]:
        score += 4
        print("correct", score)
    elif studentanswer[n] == "":
        score += 0
        print("blank", score)
    elif correctanswer[n] != studentanswer[n]:
        score -= 1
        print("incorrect", score)
if score < 0:
    score = 0
print(score) #print 6
