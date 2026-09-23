#https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/python
'''
A wolf in sheep's clothing 8 kyu

Wolves have been reintroduced to Great Britain. You are a sheep farmer, and are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them.

Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of the queue which is at the end of the array:
[sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
   7      6      5      4      3            2      1

If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.

Note: there will always be exactly one wolf in the array.

Examples
Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"

Input: ["sheep", "sheep", "wolf"]
Output: "Pls go away and stop eating my sheep"
'''
def warn_the_sheep(queue):
    if queue[-1] == 'wolf':
        return "Pls go away and stop eating my sheep"
    else:
        queuelength = len(queue)
        wolfindexnumber = queue.index("wolf") + 1 #add one because array index starts at 0
        return f'Oi! Sheep number {queuelength - wolfindexnumber}! You are about to be eaten by a wolf!'


print(warn_the_sheep(['wolf'])) #print Pls go away and stop eating my sheep
print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep'])) #print Oi! Sheep number 2! You are about to be eaten by a wolf!
print(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep'])) #print Oi! Sheep number 5! You are about to be eaten by a wolf!
print(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep'])) #print Oi! Sheep number 6! You are about to be eaten by a wolf!
print(warn_the_sheep(['sheep', 'wolf', 'sheep'])) #print Oi! Sheep number 1! You are about to be eaten by a wolf!
print(warn_the_sheep(['sheep', 'sheep', 'wolf'])) #print Pls go away and stop eating my sheep

inputsheep = ['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']
inputsheep = ["sheep", "sheep", "sheep", "wolf", "sheep"]
print(len(inputsheep)) #print 5
print(inputsheep.index("wolf")) #print 3
print(inputsheep.index("wolf") + 1) #print 4
print(len(inputsheep) - (inputsheep.index("wolf") + 1)) #print 1
