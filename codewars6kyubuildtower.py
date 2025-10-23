#https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
'''
Build Tower

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:
[
  "  *  ",
  " *** ", 
  "*****"
]

And a tower with 6 floors looks like this:
[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
'''
# numberoffloors = 6
# numberofstars = 1
# towerlist = []
# centernumber = (numberoffloors * 2) - 1
# for i in range(1, numberoffloors + 1):
#     towerblock = (numberofstars * "*").center(centernumber)
#     print(towerblock)
#     towerlist.append(towerblock)
#     numberofstars += 2
# print(towerlist)

def tower_builder(n_floors):
    numberofstars = 1
    towerlist = []
    centernumber = (n_floors * 2) - 1
    for i in range(1, n_floors + 1):
        towerblock = (numberofstars * "*").center(centernumber)
        towerlist.append(towerblock)
        numberofstars += 2
    return towerlist


print(tower_builder(3)) #print ['  *  ', ' *** ', '*****']
print(tower_builder(6)) #print ['     *     ', '    ***    ', '   *****   ', '  *******  ', ' ********* ', '***********']
