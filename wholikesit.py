#https://www.codewars.com/kata/who-likes-it
#You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
#Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:
'''
likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
For 4 or more names, the number in and 2 others simply increases.
'''
def facebooklike(names):
	namescount = len(names)
	if namescount == 0:
		print("no one likes this")
	elif namescount == 1:
		print("".join(names)+" likes this")
	elif namescount == 2:
		print(" and ".join(names)+" like this")
	elif namescount == 3:
		print(names[0]+", "+names[1]+" and "+names[2]+" like this")
	else:
		print(names[0]+", "+names[1]+" and "+str((namescount-2))+" others like this")

facebooklike([]) #print no one likes this
facebooklike(["Peter"]) #print Peter likes this
facebooklike(["Jacob", "Alex"]) #print Jacob and Alex like this
facebooklike(["Max", "John", "Mark"]) #print Max, John and Mark like this
facebooklike(["Alex", "Jacob", "Mark", "Max"]) #print Alex, Jacob and 2 others like this
facebooklike(["Ed","Al","Roy","Winry","Maes","Alexander","Izumi","mom's name I forgot"]) #print Ed, Al and 6 others like this