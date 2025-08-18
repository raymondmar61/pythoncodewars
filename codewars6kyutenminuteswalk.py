#https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
'''
Take a Ten Minutes Walk 6kyu

You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).


'''
def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    northsouthsum = walk.count("n") - walk.count("s")
    eastwestsum = walk.count("e") - walk.count("w")
    if northsouthsum == 0 and eastwestsum == 0:
        return True
    else:
        return False


print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])) #print True
print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'])) #print False
print(is_valid_walk(['w'])) #print False
print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])) #print False
print(is_valid_walk(['s', 'e', 'w', 'e', 'n', 's', 'e', 'w', 'n', 's'])) #print False
print(is_valid_walk(['n', 's', 'e', 'w', 'n', 'w', 'e', 'w', 'n', 's'])) #print False
print(is_valid_walk(['s', 'e', 'e', 'n', 'n', 's', 's', 'w', 'n', 's'])) #print False
print(is_valid_walk(['n', 'w', 'e', 'w', 'w', 's', 'e', 's', 'e', 'e'])) #print False

#A clever solution
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


directionletters = ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] #A True array
directionletters = ['n', 'w', 'e', 'w', 'e', 's', 'e', 's', 'e', 's'] #A False array
print(directionletters) #print ['n', 'w', 'e', 'w', 'e', 's', 'e', 's', 'e', 's']
print(directionletters.count("e")) #print 4
print(directionletters.count("n")) #print 1
print(directionletters.count("s")) #print 3
print(directionletters.count("w")) #print 2
print(directionletters.count("e") - directionletters.count("w")) #print 2
print(directionletters.count("n") - directionletters.count("s")) #print -2
northsouthsum = directionletters.count("n") - directionletters.count("s")
eastwestsum = directionletters.count("e") - directionletters.count("w")
if northsouthsum == 0 and eastwestsum == 0:
    print("True")
else:
    print("False") #print False

# def incorrect_is_valid_walk(walk):
#     points = 0
#     directionpoint = {"n": 1, "s": -1, "e": 1, "w": -1}
#     n = 1
#     s = -1
#     e = 1
#     w = -1
#     if len(walk) != 10:
#         return False
#     else:
#         for eachwalk in walk:
#             points = points + directionpoint.get(eachwalk)
#     if points == 0:
#         return True
#     else:
#         return False


# print(incorrect_is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])) #print True
# print(incorrect_is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'])) #print False
# print(incorrect_is_valid_walk(['w'])) #print False
# print(incorrect_is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])) #print False

# directionletters = ['s', 'e', 'w', 'e', 'n', 's', 'e', 'w', 'n', 's']
# points = 0
# directionpoint = {"n": 1, "s": -1, "e": 1, "w": -1}
# n = 1
# s = -1
# e = 1
# w = -1
# if len(directionletters) != 10:
#     print("False")
# for eachdirectionletters in directionletters:
#     print(eachdirectionletters) #print s
#     points = points + directionpoint.get(eachdirectionletters)
#     print(points) #print -1
