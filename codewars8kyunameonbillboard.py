#https://www.codewars.com/kata/570e8ec4127ad143660001fd/train/python
'''
Name on billboard 8 kyu

You can print your name on a billboard ad. Find out how much it will cost you. Each character has a default price of £30, but that can be different if you are given 2 parameters instead of 1 (always 2 for Java).

You can not use multiplier "*" operator.

If your name would be Jeong-Ho Aristotelis, ad would cost £600. 20 letters * 30 = 600 (Space counts as a character).
'''
def billboard(name, price=30):
    totalcountcharacters = len(name)
    counter = 1
    totalcost = 0
    while counter <= totalcountcharacters:
        totalcost += price
        counter += 1
    return totalcost


print(billboard("Jeong-Ho Aristotelis")) #print 600
print(billboard("Abishai Charalampos")) #print 570
print(billboard("Idwal Augustin")) #print 420
print(billboard("Hadufuns John", 20)) #print 260
print(billboard("Zoroaster Donnchadh")) #print 570
print(billboard("Claude Miljenko")) #print 450
print(billboard("Werner Vigi", 15)) #print 165
print(billboard("Anani Fridumar")) #print 420
print(billboard("Paolo Oli")) #print 270
print(billboard("Hjalmar Liupold", 40)) #print 600
print(billboard("Simon Eadwulf")) #print 390


name = "Jeong-Ho Aristotelis"
price = 30
print(len(name)) #print 20
totalcountcharacters = len(name)
counter = 1
totalcost = 0
while counter <= totalcountcharacters:
    totalcost += price
    counter += 1
print(totalcost) #print 600

#User solution
def billboard(name, price=30):
    return sum(price for letter in name)
