#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
'''
Mumbling 7kyu

This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
'''
def accum(st):
    stlist = [*st]
    stlength = len(stlist)
    answer = stlist[0].upper() + stlist[0].lower() * 0
    for n in range(1, stlength):
        answer += "-" + stlist[n].upper() + stlist[n].lower() * n
    return answer


print(accum("abcd")) #print A-Bb-Ccc-Dddd
print(accum("RqaEzty")) #print R-Qq-Aaa-EEEE-Zzzzz-Tttttt-Yyyyyyy
print(accum("cwAt")) #print C-Ww-AAA-Tttt
print(accum("ZpglnRxqenU")) #print Z-Pp-Ggg-Llll-Nnnnn-RRRRRR-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu
print(accum("NyffsGeyylB")) #print N-Yy-Fff-Ffff-Sssss-GGGGGG-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb
print(accum("MjtkuBovqrU")) #print M-Jj-Ttt-Kkkk-Uuuuu-BBBBBB-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu
print(accum("EvidjUnokmM")) #print E-Vv-Iii-Dddd-Jjjjj-UUUUUU-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm
print(accum("HbideVbxncC")) #print H-Bb-Iii-Dddd-Eeeee-VVVVVV-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc

print("a" * 0 + "b" * 1) #print b
print("a" * 1) #print a
print("a" * 2) #print aa
mumble = "abcd"
mumblelist = [*mumble]
print(mumblelist) #print ['a', 'b', 'c', 'd']
print(mumblelist[0].upper() + "-" + mumblelist[1].upper() + (mumblelist[1].lower() * 1) + "-" + mumblelist[2].upper() + (mumblelist[2].lower() * 2) + "-" + mumblelist[3].upper() + (mumblelist[3].lower() * 3)) #print A-Bb-Ccc-Dddd
mumblelength = len(mumblelist)
print(mumblelength) #print 4
answer = mumblelist[0].upper() + mumblelist[0].lower() * 0
print(answer) #print A
for n in range(1, mumblelength):
    print("-" + mumblelist[n].upper() + mumblelist[n].lower() * n)
    answer += "-" + mumblelist[n].upper() + mumblelist[n].lower() * n
    '''
    -Bb
    -Ccc
    -Dddd
    '''
print(answer) #print A-Bb-Ccc-Dddd