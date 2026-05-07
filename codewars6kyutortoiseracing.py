#https://www.codewars.com/kata/55e2adece53b4cdcb900006c/train/python
'''
Tortoise racing 6 kyu

Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour. Young B knows she runs faster than A, and furthermore has not finished her cabbage.

When she [B] starts, at last, she can see that A has a 70 feet lead but B's speed is 850 feet per hour. How long will it take B to catch A?

More generally: given two speeds v1 (A's speed, integer > 0) and v2 (B's speed, integer > 0) and a lead g (integer > 0) how long will it take B to catch A?

The result will be an array [hour, min, sec] which is the time needed in hours, minutes and seconds (round down to the nearest second) or a string in some languages.

If v1 >= v2 then return nil, nothing, null, None or {-1, -1, -1} for C++, C, Go, Nim, Pascal, COBOL, Erlang, [-1, -1, -1] for Perl,[] for Kotlin or "-1 -1 -1" for others.

Examples:
(form of the result depends on the language)

race(720, 850, 70) => [0, 32, 18] or "0 32 18"
race(80, 91, 37)   => [3, 21, 49] or "3 21 49"

Note:
See other examples in "Your test cases".

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.

** Hints for people who don't know how to convert to hours, minutes, seconds:

Tortoises don't care about fractions of seconds
Think of calculation by hand using only integers (in your code use or simulate integer division)
or Google: "convert decimal time to hours minutes seconds"

RM:  https://www.vcalc.com/wiki/time-to-overtake.  time=distance between objects/(speed of vehicle chasing initial vehicle - speed of vehicle initially started)
'''
def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        time = g / (v2 - v1)
        #Convert time to seconds by multiplying by 3600 returning an integer
        timeinseconds = int(time * 3600)
        hours = timeinseconds // 3600
        minutes = (timeinseconds % 3600) // 60
        seconds = timeinseconds % 60
    return [hours, minutes, seconds]


print(race(720, 850, 70)) #print [0, 32, 18]
print(race(80, 91, 37)) #print [3, 21, 49]
print(race(820, 81, 550)) #print None

#Not accurate because of rounding errors.  CodeWars incorrect hour, minute, or second off by +1.
def raceinaccurate(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        time = g / (v2 - v1)
        hour = int(time)
        minute = int((time % 1) * 60)
        second = int(((time * 60) % 1) * 60)
        return [hour, minute, second]


print(raceinaccurate(720, 850, 70)) #print [0, 32, 18]
print(raceinaccurate(80, 91, 37)) #print [3, 21, 49]
print(raceinaccurate(820, 81, 550)) #print None


v1 = 80
v2 = 91
g = 37
time = g / (v2 - v1)
print(time) #print 3.3636363636363638.  Total time in hours.
print(int(time)) #print 3.  Extract left of decimal.
print(time % 1) #print 0.36363636363636376.  Extract the decimal hours.
print((time % 1) * 60) #print 21.818181818181827.  Convert extracted decimal hours to minutes.
print(int((time % 1) * 60)) #print 21.  Extract left of decimal for minutes.
print((time * 60) % 1) #print 0.818181818181813.  Extract decimal minutes
print(((time * 60) % 1) * 60) #print 49.09090909090878.  Convert extracted decimal minutes to seconds.
print(int(((time * 60) % 1) * 60)) #print 49.  Extract left of decimal.
print("\n")

v1 = 720
v2 = 850
g = 70

time = g / (v2 - v1)
print(time) #print 0.5384615384615384  Total time in hours.
print(int(time)) #print 0.  Extract left of decimal.
print(time % 1) #print 0.5384615384615384.  Extract the decimal hours.
print((time % 1) * 60) #print 32.30769230769231.  Convert extracted decimal hours to minutes.
print(int((time % 1) * 60)) #print 32.  Extract left of decimal for minutes.
print((time * 60) % 1) #print 0.3076923076923066.  Extract decimal minutes
print(((time * 60) % 1) * 60) #print 18.461538461538396.  Convert extracted decimal minutes to seconds.
print(int(((time * 60) % 1) * 60)) #print 18.  Extract left of decimal.

v1 = 720
v2 = 850
g = 70

time = g / (v2 - v1)
hour = int(time)
minute = int((time % 1) * 60)
second = int(((time * 60) % 1) * 60)
print([hour, minute, second]) #print [0, 32, 18]

#User solutions
from datetime import datetime, timedelta

def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        sec = timedelta(seconds=int((g * 3600 / (v2 - v1))))
        d = datetime(1, 1, 1) + sec

        return [d.hour, d.minute, d.second]

def race(v1, v2, g):
    t = 3600 * g / (v2 - v1)
    return [t / 3600, t / 60 % 60, t % 60] if v2 > v1 else None

def race(v1, v2, g):
    if v1 >= v2:
        return None
    t = float(g) / (v2 - v1) * 3600
    mn, s = divmod(t, 60)
    h, mn = divmod(mn, 60)
    return [int(h), int(mn), int(s)]

def race(v1, v2, g):
    if v1 < v2:
        sec = g * 60 * 60 // (v2 - v1)
        return [sec // 3600, sec // 60 % 60, sec % 60]
