#https://www.codewars.com/kata/5aa736a455f906981800360d/train/python
'''
The Feast of Many Beasts 8 kyu

All of the animals are having a feast! Each animal is bringing one dish. There is just one rule: the dish must start and end with the same letters as the animal's name. For example, the great blue heron is bringing garlic naan and the chickadee is bringing chocolate cake.

Write a function feast that takes the animal's name and dish as arguments and returns true or false to indicate whether the beast is allowed to bring the dish to the feast.

Assume that beast and dish are always lowercase strings, and that each has at least two letters. beast and dish may contain hyphens and spaces, but these will not appear at the beginning or end of the string. They will not contain numerals.
'''
def feast(beast, dish):
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False


print(feast("great blue heron", "garlic naan")) #print  True
print(feast("chickadee", "chocolate cake")) #print  True
print(feast("brown bear", "bear claw")) #print  False

beast = "chickadee"
dish = "chocolate cake"
print(beast[0]) #print c
print(beast[-1]) #print e
print(dish[0]) #print c
print(dish[-1]) #print e
if beast[0] == dish[0] and beast[-1] == dish[-1]:
    print("True") #print True
else:
    print("False")

beast = "brown bear"
dish = "bear claw"
print(beast[0]) #print b
print(beast[-1]) #print r
print(dish[0]) #print b
print(dish[-1]) #print w
if beast[0] == dish[0] and beast[-1] == dish[-1]:
    print("True")
else:
    print("False")  #print False
