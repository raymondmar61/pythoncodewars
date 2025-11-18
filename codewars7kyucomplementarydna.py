#https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python
'''
Complementary DNA 7kyu

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
'''
def DNA_strand(dna):
    complementarydnadictionary = {"A": "T", "T": "A", "C": "G", "G": "C"}
    dnastringlist = [*dna]
    dnastringoutput = "".join([complementarydnadictionary[eachdnastringlist] for eachdnastringlist in dnastringlist])
    return dnastringoutput


print(DNA_strand("ATTGC")) #print TAACG
print(DNA_strand("GTAT")) #print CATA
print(DNA_strand("AAAA")) #print TTTT


complementarydnadictionary = {"A": "T", "T": "A", "C": "G", "G": "C"}
dnastring = "ATTGC"
dnastringlist = [*dnastring]
print(dnastringlist) #print ['A', 'T', 'T', 'G', 'C']
for eachdnastringlist in dnastringlist:
    print(complementarydnadictionary[eachdnastringlist])
    '''
    T
    A
    A
    C
    G
    '''
dnastringoutput = "".join([complementarydnadictionary[eachdnastringlist] for eachdnastringlist in dnastringlist])
print(dnastringoutput) #print TAACG

#User solution
import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG", "TAGC"))
