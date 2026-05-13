#https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python
'''
Switch it Up! 8 kyu

When provided with a number between 0-9, return it in words. Note that the input is guaranteed to be within the range of 0-9.

Input: 1

Output: "One".
'''
def switch_it_up(number):
    numberwords = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return numberwords[number]


print(switch_it_up(0)) #print Zero
print(switch_it_up(9)) #print Nine

#User submission
def switch_it_up(n):
    return ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][n]
