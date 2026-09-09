#https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python
'''
Help the bookseller ! 6 kyu

A bookseller has lots of books classified in 26 categories labeled A, B, C, ..., Z. Each book has a code of at least 3 characters. The 1st character of a code is a capital letter which defines the book category.

In the bookseller's stocklist each code is followed by a space and by a positive integer, which indicates the quantity of books of this code in stock.

Task
You will receive the bookseller's stocklist and a list of categories. Your task is to find the total number of books in the bookseller's stocklist, with the category codes in the list of categories. Note: the codes are in the same order in both lists.

Return the result as a string described in the example below, or as a list of pairs (Haskell/Clojure/Racket/Prolog).

If any of the input lists is empty, return an empty string, or an empty array/list (Clojure/Racket/Prolog).

Example
# the bookseller's stocklist:
"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"

# list of categories: 
"A", "B", "C", "W"

# result:
"(A : 20) - (B : 114) - (C : 50) - (W : 0)"
Explanation:

category A: 20 books (ABART)
category B: 114 books = 25 (BKWRK) + 89 (BTSQZ)
category C: 50 books (CDXEF)
category W: 0 books
'''
def stock_list(stocklist, categories):
    #stocklist empty or categories empty return empty string
    if stocklist == [] or categories == []:
        return ""
    #Create dictionary from the categories list
    categoriesdictionary = {}
    for eachcategories in categories:
        categoriesdictionary[eachcategories] = 0
    #Add books and quantity to categoriesdictionary
    for eachstocklist in stocklist:
        eachstocklistsplit = eachstocklist.split()
        eachstocklistsplitcategory = eachstocklistsplit[0][0]
        eachstocklistsplitquantity = int(eachstocklistsplit[1])
        if eachstocklistsplitcategory not in categories:
            pass
        else:
            categoriesdictionary[eachstocklistsplitcategory] = categoriesdictionary[eachstocklistsplitcategory] + eachstocklistsplitquantity

    #Final output result as string
    result = ""
    for key, value in categoriesdictionary.items():
        resultformat = (f"({key} : {value}) - ")
        result = result + resultformat
    return result[:-3]


print(stock_list(["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"], ["A", "B", "C", "W"])) #print (A : 20) - (B : 114) - (C : 50) - (W : 0)
print(stock_list(["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"], [])) #print
print(stock_list([], ["A", "B", "C", "W"])) #print
print(stock_list(["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B", "C", "D"])) #print (A : 0) - (B : 1290) - (C : 515) - (D : 600)
print(stock_list(["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B"])) #print (A : 200) - (B : 1140)

'''
stocklist = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
categories = ["A", "B", "C", "W"]
categoriesdictionary = {}
#Create dictionary from the categories list
for eachcategories in categories:
    categoriesdictionary[eachcategories] = 0
print(categoriesdictionary) #print {'A': 0, 'B': 0, 'C': 0, 'W': 0}
print(categoriesdictionary["A"]) #print 0
categoriesdictionary["A"] = 50
print(categoriesdictionary["A"]) #print 50
print(categoriesdictionary) #print {'A': 50, 'B': 0, 'C': 0, 'W': 0}
#Add books and quantity to categoriesdictionary
for eachstocklist in stocklist:
    print(eachstocklist) #print ABART 20
    print(eachstocklist.split()) #print ['ABART', '20']
    eachstocklistsplit = eachstocklist.split()
    eachstocklistsplitcategory = eachstocklistsplit[0][0]
    eachstocklistsplitquantity = int(eachstocklistsplit[1])
    if eachstocklistsplitcategory not in categories:
        pass
    else:
        categoriesdictionary[eachstocklistsplitcategory] = categoriesdictionary[eachstocklistsplitcategory] + eachstocklistsplitquantity
print(categoriesdictionary) #print {'A': 20, 'B': 114, 'C': 50, 'W': 0}
#Final output result as string
result = ""
for key, value in categoriesdictionary.items():
    print(f"({key} : {value}) - ") #print (A : 20) -
    resultformat = (f"({key} : {value}) - ")
    result = result + resultformat
print(result[:-3]) #print (A : 20) - (B : 114) - (C : 50) - (W : 0)
print(type(result[:-3])) #print <class 'str'>
'''
