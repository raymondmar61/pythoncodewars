#https://www.codewars.com/kata/55cb632c1a5d7b3ad0000145/train/python
'''
Keep up the hoop 8kyu

Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him.

Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message:

If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
If he doesn't get 10 hoops, return the string "Keep at it until you get it".
'''
def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"


print(hoop_count(10)) #print Great, now move on to tricks
print(hoop_count(11)) #print Great, now move on to tricks
print(hoop_count(9)) #print Keep at it until you get it

#Alternate answer
def hoopCount(n):
    return "Keep at it until you get it" if n<10 else "Great, now move on to tricks"