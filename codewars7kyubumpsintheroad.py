#https://www.codewars.com/kata/57ed30dde7728215300005fa/train/python
'''
Bumps in the Road 7 kyu

Your car is old, it breaks easily. The shock absorbers are gone and you think it can handle about 15 more bumps before it dies totally.

Unfortunately for you, your drive is very bumpy! Given a string showing either flat road (_) or bumps (n). If you are able to reach home safely by encountering 15 bumps or less, return Woohoo!, otherwise return Car Dead
'''
def bumps(road):
    bumpcounter = road.count("n")
    if bumpcounter <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"


print(bumps("n")) #print Woohoo!
print(bumps("__nn_nnnn__n_n___n____nn__nnn")) #print Woohoo!
print(bumps("nnn_n__n_n___nnnnn___n__nnn__")) #print Woohoo!
print(bumps("_nnnnnnn_n__n______nn__nn_nnn")) #print Car Dead
print(bumps("______n___n_")) #print Woohoo!
print(bumps("nnnnnnnnnnnnnnnnnnnnn")) #print Car Dead

test = "__nn___n"
print(test.count("n")) #print 3
