#https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python
'''
Is the string uppercase? 8kyu

Task
Create a method to see whether the string is ALL CAPS.

Examples (input -> output)
"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True

In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.
'''
def is_uppercase(inp):
    for eachinp in inp:
        if eachinp.islower():
            return False
    return True


print(is_uppercase("c")) #print False
print(is_uppercase("C")) #print True
print(is_uppercase("hello I AM DONALD")) #print False
print(is_uppercase("HELLO I AM DONALD")) #print True
print(is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ")) #print False
print(is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ")) #print True
print(is_uppercase("$%&")) #print True
print(is_uppercase("in|")) #print False
print(is_uppercase("[)*p538Ik@O!Gr&hK`^")) #print False
print(is_uppercase("kSF,")) #print False
print(is_uppercase("3j^9m[i8C\\Zr>$Ou(J~")) #print False
print(is_uppercase("\\z$)GT6M<LiUb&H;P|^aR4Z)]O_qr.Wyd`_K@h!+Xw\"E")) #print False
print(is_uppercase("w5")) #print False
print(is_uppercase(",;Jr`)#^&N$fj4ck@ nS:_CpvW.Q<u[adAlZ97M30/U\"zXh+RK")) #print False

#User submission
def is_uppercase(inp):
    return inp.upper() == inp
