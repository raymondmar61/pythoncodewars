#https://www.codewars.com/kata/577ff15ad648a14b780000e7/train/python
'''
Welcome! 8kyu

Your start-up's BA has told marketing that your website has a large audience in Scandinavia and surrounding countries. Marketing thinks it would be great to welcome visitors to the site in their own language. Luckily you already use an API that detects the user's location, so this is an easy win.

The Task
Think of a way to store the languages as a database. The languages are listed below so you can copy and paste!
Write a 'welcome' function that takes a parameter 'language', with a type String, and returns a greeting - if you have it in your database. It should default to English if the language is not in the database, or in the event of an invalid input.

The Database
Please modify this as appropriate for your language.
[ ("english", "Welcome") , ("czech", "Vitejte") , ("danish", "Velkomst") , ("dutch", "Welkom") , ("estonian", "Tere tulemast") , ("finnish", "Tervetuloa") , ("flemish", "Welgekomen") , ("french", "Bienvenue") , ("german", "Willkommen") , ("irish", "Failte") , ("italian", "Benvenuto") , ("latvian", "Gaidits") , ("lithuanian", "Laukiamas") , ("polish", "Witamy") , ("spanish", "Bienvenido") , ("swedish", "Valkommen") , ("welsh", "Croeso") ]

Possible invalid inputs include:

IP_ADDRESS_INVALID - not a valid ipv4 or ipv6 ip address
IP_ADDRESS_NOT_FOUND - ip address not in the database
IP_ADDRESS_REQUIRED - no ip address was supplied
'''
def greet(language):
    databaselanguages = {"english": "Welcome", "czech": "Vitejte", "danish": "Velkomst", "dutch": "Welkom", "estonian": "Tere tulemast", "finnish": "Tervetuloa", "flemish": "Welgekomen", "french": "Bienvenue", "german": "Willkommen", "irish": "Failte", "italian": "Benvenuto", "latvian": "Gaidits", "lithuanian": "Laukiamas", "polish": "Witamy", "spanish": "Bienvenido", "swedish": "Valkommen", "welsh": "Croeso"}
    if language not in databaselanguages.keys():
        return "Welcome"
    else:
        return databaselanguages[language]


print(greet("english")) #print Welcome
print(greet("italian")) #print Benvenuto
print(greet("japanese")) #print Welcome

#Most popular submittal
def greet(language):
    return {'czech': 'Vitejte', 'danish': 'Velkomst', 'dutch': 'Welkom', 'english': 'Welcome', 'estonian': 'Tere tulemast', 'finnish': 'Tervetuloa', 'flemish': 'Welgekomen', 'french': 'Bienvenue', 'german': 'Willkommen', 'irish': 'Failte', 'italian': 'Benvenuto', 'latvian': 'Gaidits', 'lithuanian': 'Laukiamas', 'polish': 'Witamy', 'spanish': 'Bienvenido', 'swedish': 'Valkommen', 'welsh': 'Croeso'}.get(language, 'Welcome default value if language not in dictionary')


print(greet("not a language")) #print Welcome default value if language not in dictionary.  The get() method returns the value matching the key.  If there is no match, the get method returns the default value.
