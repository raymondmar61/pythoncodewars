#https://www.codewars.com/kata/58649884a1659ed6cb000072/train/python
'''
Thinkful - Logic Drills: Traffic light 8kyu

You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

For example, when the input is green, output should be yellow.
'''
def update_light(current):
    lightchangedictionary = {"green": "yellow", "yellow": "red", "red": "green"}
    return lightchangedictionary[current]


print(update_light("green")) #print yellow
print(update_light("yellow")) #print red
print(update_light("red")) #print green

'''
Top solution
def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]
'''