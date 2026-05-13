#https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/python
'''
Reverse or rotate? 6 kyu

The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If the sum of a chunk's digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If

sz is <= 0 or if str == "" return ""
sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".

Examples:
("123456987654", 6) --> "234561876549"
("123456987653", 6) --> "234561356789"
("66443875", 4) --> "44668753"
("66443875", 8) --> "64438756"
("664438769", 8) --> "67834466"
("123456779", 8) --> "23456771"
("", 8) --> ""
("123456779", 0) --> ""
("563000655734469485", 4) --> "0365065073456944"

Example of a string rotated to the left by one position:
s = "123456" gives "234561".
'''
def rev_rot(strng, sz):
    answer = ""
    if (len(strng) < sz) or (sz <= 0) or (strng == ""):
        return answer
    else:
        for i in range(0, len(strng), sz):
            chunk = strng[i:i + sz] #print 123456\n 987654
            if len(chunk) < sz:
                pass
            else:
                chunksum = 0
                for eachchunk in chunk:
                    chunksum = int(eachchunk) + chunksum
                if chunksum % 2 == 0:
                    reverse = chunk[::-1]
                    answer += reverse
                else:
                    rotate = chunk[1:] + chunk[0]
                    answer += rotate
        return answer


print(rev_rot("1234", 0)) #print """
print(rev_rot("", 0)) #print ""
print(rev_rot("1234", 5)) #print ""
print(rev_rot("733049910872815764", 5)) #print 330479108928157
print(rev_rot("123456987654", 6)) #print 234561876549
print(rev_rot("123456987653", 6)) #print 234561356789
print(rev_rot("66443875", 4)) #print 44668753
print(rev_rot("66443875", 8)) #print 64438756
print(rev_rot("664438769", 8)) #print 67834466
print(rev_rot("123456779", 8)) #print 23456771
print(rev_rot("", 8)) #print ""
print(rev_rot("123456779", 0)) #print ""
print(rev_rot("563000655734469485", 4)) #print 0365065073456944

strng = "123456987654"
sz = 6
answer = ""
print(len(strng)) #print 12
if (len(strng) < sz) or (sz <= 0) or (strng == ""):
    print("love")
else:
    for i in range(0, len(strng), sz):
        chunk = strng[i:i + sz] #print 123456\n 987654
        print(chunk) #print 123456
        print(type(chunk)) #print <class 'str'>
        if len(chunk) < sz:
            pass
        else:
            chunksum = 0
            for eachchunk in chunk:
                print(eachchunk) #print1\n 2\n 3\n 4\n 5\n 6
                chunksum = int(eachchunk) + chunksum
            print(f"chunksum {chunksum}") #print 21
            if chunksum % 2 == 0:
                reverse = chunk[::-1]
                print(reverse)
                answer += reverse
            else:
                rotate = chunk[1:] + chunk[0]
                print(rotate) #print 234561
                answer += rotate

print(answer) #print 234561876549
print(type(answer)) #print <class 'str'>

strng = "123456987654"
sz = 6
#Split string by number of characters or every nth character.  Google AI and https://stackoverflow.com/questions/9475241/split-string-every-nth-character
for i in range(0, len(strng), sz):
    print(i) #print 0\n 6
for i in range(0, len(strng), sz):
    print(strng[i:i + sz]) #print 123456\n 987654
listcomprehensionsplitstring = [strng[i:i + sz] for i in range(0, len(strng), sz)]
print(listcomprehensionsplitstring) #print ['123456', '987654']
import textwrap
chunks = textwrap.wrap(strng, width=sz)
print(chunks) #print ['123456', '987654']
import re #RM:  doesn't work if the string contain newlines
chunksregularexpressions = re.findall(f".{{1,{sz}}}", strng)
print(chunksregularexpressions) #print ['123456', '987654']
chunksregularexpressions2 = re.findall(("." * sz), strng)
print(chunksregularexpressions2) #print ['123456', '987654']
chunksregularexpressions3 = re.findall("......?", strng)
print(chunksregularexpressions3) #print ['123456', '987654']
chunksregularexpressions4 = re.findall(".{1,6}", strng)
print(chunksregularexpressions4) #print ['123456', '987654']