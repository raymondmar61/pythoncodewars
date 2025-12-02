#https://www.codewars.com/kata/57ec8bd8f670e9a47a000f89/train/python
'''
The Wide-Mouthed frog! 8kyu

The wide-mouth frog is particularly interested in the eating habits of other creatures.

He just can't stop asking the creatures he encounters what they like to eat. But, then he meets the alligator who just LOVES to eat wide-mouthed frogs!

When he meets the alligator, it then makes a tiny mouth.

Your goal in this kata is to create complete the mouth_size method this method takes one argument animal which corresponds to the animal encountered by the frog. If this one is an alligator (case-insensitive) return small otherwise return wide.
'''
def mouth_size(animal):
    if animal.lower() == "alligator":
        return "small"
    else:
        return "wide"
print(mouth_size("toucan")) #print wide
print(mouth_size("ant bear")) #print wide
print(mouth_size("alligator")) #print small

animal = "ALLIGATOR"
if animal.lower() == "alligator":
    print("small") #print small
else:
    print("wide")

#User submission
def mouth_size(animal): 
    return 'small' if animal.lower() == 'alligator' else 'wide'