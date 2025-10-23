#https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python
'''
Are You Playing Banjo? 8kyu

Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"

Names given are always valid strings.
'''
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


print(are_you_playing_banjo("Raymond")) #print Raymond plays banjo
print(are_you_playing_banjo("raymond")) #print raymond plays banjo
print(are_you_playing_banjo("Kaymond")) #print Kaymond does not play banjo
print(are_you_playing_banjo("kaymond")) #print kaymond does not play banjo

yesrname = "Raymond"
norname = "kaymond"

if yesrname[0].lower() == "r":
    print(yesrname + " plays banjo") #print Raymond plays banjo
else:
    print(name + " does not play banjo")
