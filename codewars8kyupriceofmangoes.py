#https://www.codewars.com/kata/57a77726bb9944d000000b06/train/python
'''
Price of Mangoes 8 kyu

Accountant time! For a given quantity and price (per mango), calculate the total cost of the mangoes.
But! Every third mango is free!

Examples

Quantity = 2
Price = 3
Total cost ==> 6    
# Paid 2 mangoes for $3 per unit = $6; no mango for free

Quantity = 3
Price = 3
Total cost ==> 6    
# Paid 2 mangoes for $3 per unit = $6; +1 mango for free

Quantity = 5
Price = 3
Total cost ==> 12   
# Paid 4 mangoes for $3 per unit = $12; +1 mango for free

Quantity = 9
Price = 5
Total cost ==> 30   
# Paid 6 mangoes for $5 per unit = $30; +3 mangoes for free
'''
def mango(quantity, price):
    totalcost = 0
    for x in range(1, quantity + 1):
        if x % 3 == 0:
            pass
        else:
            totalcost += price
    return totalcost


print(mango(3, 3)) #print 6
print(mango(9, 5)) #print 30

quantity = 9
price = 5
totalcost = 0
for x in range(1, quantity + 1):
    if x % 3 == 0:
        pass
    else:
        totalcost += price
print(totalcost) #print 30

#User solution
def mango(quantity, price):
    return (quantity - quantity // 3) * price
