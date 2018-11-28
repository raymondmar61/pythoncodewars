#https://www.codewars.com/kata/decode-the-morse-code
#The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.
#NOTE: Extra spaces before or after the code have no meaning and should be ignored.
#Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.  For example:  decodeMorse('.... . -.--   .--- ..- -.. .') returns "HEY JUDE"
#Morse Code Dictionary source https://www.geeksforgeeks.org/morse-code-translator-python/
morsecodedictionary = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'," ":" ", " ":""}
#additional sources https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary, https://stackoverflow.com/questions/16228248/how-can-i-get-list-of-values-from-dict
#print(list(morsecodedictionary.values())) #print ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----', '--..--', '.-.-.-', '..--..', '-..-.', '-....-', '-.--.', '-.--.-', ' '] source: https://stackoverflow.com/questions/16228248/how-can-i-get-list-of-values-from-dict

def decodemorsecode(morsecode):
	morsecodeword = ""
	morsecode = morsecode.upper()
	morsecodelist = morsecode.split(" ")
	for eachmorsecodelist in morsecodelist:
		morsecodeword = morsecodeword + list(morsecodedictionary.keys())[list(morsecodedictionary.values()).index(eachmorsecodelist)]
	from re import sub
	return sub(' +', ' ',morsecodeword)

def codemorsecode(word):
	word = word.upper()
	wordmorsecode = ""
	for eachword in word:	
		wordmorsecode = wordmorsecode + morsecodedictionary[eachword]+" "
	return wordmorsecode

print(codemorsecode("Let It Be")) #print .-.. . -  .. -  -... . 
print(decodemorsecode(".... . -.--   .--- ..- -.. .")) #print HEY JUDE
doublecheck = codemorsecode("Let It Be")
print(decodemorsecode(doublecheck)) #print LET IT BE