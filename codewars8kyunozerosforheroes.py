#https://www.codewars.com/kata/570a6a46455d08ff8d001002/train/python
'''
No zeros for heroes 8kyu

Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450   -> 145
960000 -> 96
1050   -> 105
-1050  -> -105
0      -> 0

Note: Zero should be left as it is.
'''
def no_boring_zeros(n):
    counter = 0
    for eachnumber in str(n)[::-1]:
        if eachnumber == "0":
            counter += 1
        if eachnumber != "0":
            break
    divisor = 10 ** counter
    return (n // divisor)


print(no_boring_zeros(1450)) #print 145
print(no_boring_zeros(960000)) #print 96
print(no_boring_zeros(1050)) #print 105
print(no_boring_zeros(-1050)) #print -105
print(no_boring_zeros(0)) #print 0
print(no_boring_zeros(2016)) #print 2016

number = 1050
counter = 0
for eachnumber in str(number)[::-1]:
    if eachnumber == "0":
        print(eachnumber) #print 0
        counter += 1
    if eachnumber != "0":
        break
    print(counter) #print 1
divisor = 10 ** counter
print(number // divisor) #print 105

#User submission
def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0
