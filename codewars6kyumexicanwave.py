#https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
'''
Mexican Wave 6kyu

Introduction
The wave (known as the Mexican wave in the English-speaking world outside North America) is an example of metachronal rhythm achieved in a packed stadium when successive groups of spectators briefly stand, yell, and raise their arms. Immediately upon stretching to full height, the spectator returns to the usual seated position. The result is a wave of standing spectators that travels through the crowd, even though individual spectators never move away from their seats. In many large arenas the crowd is seated in a contiguous circuit all the way around the sport field, and so the wave is able to travel continuously around the arena; in discontiguous seating arrangements, the wave can instead reflect back and forth through the crowd. When the gap in seating is narrow, the wave can sometimes pass through it. Usually only one wave crest will be present at any given time in an arena, although simultaneous, counter-rotating waves have been produced.

Task
In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return an array of strings where an uppercase letter is a person standing up.

Rules
1.  The input string will always consist of lowercase letters and spaces, but may be empty, in which case you must return an empty array.
2.  If the character in the string is whitespace then pass over it as if it was an empty seat.

Examples
"hello" => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
" s p a c e s " => [ " S p a c e s ", " s P a c e s ", " s p A c e s ", " s p a C e s ", " s p a c E s ", " s p a c e S "]
'''
def wave(people):
    numberofwaves = len(people)
    splitpeople = [*people]
    wavelist = []
    for n in range(0, numberofwaves):
        if splitpeople[n] == " ":
            pass
        else:
            letternumber = 0
            createwaveletter = []
            for eachletter in splitpeople:
                if letternumber == n:
                    createwaveletter.append(eachletter.upper())
                else:
                    createwaveletter.append(eachletter)
                letternumber += 1
            wavelist.append("".join(createwaveletter))
    return wavelist


print(wave("codewars")) #print ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"])
print(wave("")) #print []
print(wave("two words")) #print ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two printwordS"]
print(wave(" gap ")) #print [" Gap ", " gAp ", " gaP "]
print(wave("a       b    ")) #print ["A       b    ", "a       B    "]
print(wave("this is a few words")) #print ["This is a few words", "tHis is a few words", "thIs is a few words", "thiS is a few words", "this Is a few words", "this iS a few words", "this is A few words", "this is a Few words", "this is a fEw words", "this is a feW words", "this is a few Words", "this is a few wOrds", "this is a few woRds", "this is a few worDs", "this is a few wordS"]


peopleword = " s p a c e s "
numberofwaves = len(peopleword)
print(numberofwaves)  #print 13
splitpeopleword = [*peopleword]
wavelist = []
for n in range(0, numberofwaves):
    print(n) #print 1
    print(splitpeopleword) #print [' ', 's', ' ', 'p', ' ', 'a', ' ', 'c', ' ', 'e', ' ', 's', ' ']
    if splitpeopleword[n] == " ":
        pass
    else:
        letternumber = 0
        createwaveletter = []
        for eachletter in splitpeopleword:
            if letternumber == n:
                print(eachletter.upper()) #print S
                createwaveletter.append(eachletter.upper())
            else:
                print(eachletter) #print p\n
                createwaveletter.append(eachletter)
            letternumber += 1
        print(createwaveletter) #print [' ', 'S', ' ', 'p', ' ', 'a', ' ', 'c', ' ', 'e', ' ', 's', ' ']
        wavelist.append("".join(createwaveletter))
print(wavelist) #print [' S p a c e s ', ' s P a c e s ', ' s p A c e s ', ' s p a C e s ', ' s p a c E s ', ' s p a c e S ']

#User submission
def wave(str):
    return [str[:i] + str[i].upper() + str[i + 1:] for i in range(len(str)) if str[i].isalpha()]
