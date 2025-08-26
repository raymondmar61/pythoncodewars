#https://www.codewars.com/kata/5601409514fc93442500010b
'''
How good are you really? 8kyu

There was a test in your class and you passed it. Congratulations!

But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return true if you're better, else false!

Note:
Your points are not included in the array of your class's points. Do not forget them when calculating the average score!
'''
def better_than_average(class_points, your_points):
    totalclasspoints = sum(class_points)
    countclasspoints = len(class_points)
    averageclasspoints = totalclasspoints / countclasspoints
    return True if your_points > averageclasspoints else False


print(better_than_average([2, 3], 5)) #print True
print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75)) #print True
print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69)) #print True
print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50)) #print False
print(better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21)) #print False
print(better_than_average([100, 90, 80], 85)) #print False
print(better_than_average([50, 50, 50], 50)) #print False

peertestscores = [2, 3]
yourtestscore = 5

print(sum(peertestscores)) #print 5
print(len(peertestscores)) #print 2
print(sum(peertestscores) / len(peertestscores)) #print 2.5
print(yourtestscore > (sum(peertestscores) / len(peertestscores))) #print True
