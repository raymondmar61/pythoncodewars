#https://www.codewars.com/kata/57675f3dedc6f728ee000256/train/python
'''
Build Tower Advanced

Build Tower by the following given arguments:  number of floors (integer and always greater than 0) and block size (width, height) (integer pair and always greater than (0, 0)).  RM:  I guess block size width must be an even number.

Tower block unit is represented as *. Tower blocks of block size (2, 1) and (2, 3) would look like respectively:

  **

  **
  **
  **

for example, a tower of 3 floors with block size = (2, 3) looks like below RM: 2, 6, 10

[
  '    **    ',
  '    **    ',
  '    **    ',
  '  ******  ',
  '  ******  ',
  '  ******  ',
  '**********',
  '**********',
  '**********'
]

RM:  block size = (width or number of blocks per floor, height or number of blocks per floor set)

and a tower of 6 floors with block size = (2, 1) looks like below RM:  2, 6, 10, 14, 18, 22

[
  '          **          ',
  '        ******        ',
  '      **********      ',
  '    **************    ',
  '  ******************  ',
  '**********************'
]

Don't return a whole string containing line-endings but a list/array/vector of strings instead!

This kata might looks like a 5.5kyu one. So challenge yourself!
'''
def tower_builder(n_floors, block_size):
    numberoffloors = n_floors
    width = block_size[0]
    height = block_size[1]
    widthnumberofstars = width
    centernumber = [x for x in range(1, (numberoffloors * 2))][-1] * width
    multiplier = 1
    towerlist = []
    for floornumber in range(1, numberoffloors + 1):
        for heightnumber in range(1, height + 1):
            towerblock = (widthnumberofstars * "*").center(centernumber)
            towerlist.append(towerblock)
        multiplier += 2
        widthnumberofstars = width * multiplier
    return towerlist


print(tower_builder(1, (2, 1))) #print ['**']
print(tower_builder(1, (2, 3))) #print ['**', '**', '**']
print(tower_builder(3, (2, 3))) #print ['    **    ', '    **    ', '    **    ', '  ******  ', '  ******  ', '  ******  ', '**********', '**********', '**********']
print(tower_builder(6, (2, 1))) #print ['          **          ', '        ******        ', '      **********      ', '    **************    ', '  ******************  ', '**********************']