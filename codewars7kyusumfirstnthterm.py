#https://www.codewars.com/kata/555eded1ad94b00403000071/train/python
'''
Sum of the first nth term of Series 7kyu

Your task is to write a function which returns the n-th term of the following series, which is the sum of the first n terms of the sequence (n is the input parameter).

Series:  1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + . . .

You will need to figure out the rule of the series to complete this.

Rules
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return "0.00".

You will only be given Natural Numbers as arguments.

Examples (Input --> Output)
n
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
'''
def series_sum(n):
    if n == 0:
        sumanswer = ("%.2f" % 0.00)
        return sumanswer
    sumserieslist = []
    counter = 1
    denominator = 1
    while counter <= n:
        sumserieslist.append("1/" + str(denominator))
        denominator += 3
        counter += 1
    sumnthterm = 1 / 1
    for eachfraciton in sumserieslist[1:]:
        nthterm = int(1) / int(eachfraciton[2:])
        sumnthterm += nthterm
    sumanswer = round(sumnthterm, 2)
    return ("%.2f" % sumanswer)


print(series_sum(0)) #print 0.00
print(series_sum(1)) #print 1.00
print(series_sum(2)) #print 1.25
print(series_sum(5)) #print 1.57

print("%.2f" % (1 / 1)) #print 1.00
print((1 / 1) + (1 / 4)) #print 1.25
print((1 / 1) + (1 / 4) + (1 / 7) + (1 / 10) + (1 / 13)) #print 1.5697802197802198
roundtwodecimalplaces = (1 + (1 / 4) + (1 / 7) + (1 / 10) + (1 / 13))
print(round(roundtwodecimalplaces, 2)) #print 1.57
print("%.2f" % roundtwodecimalplaces) #print 1.57
sumserieslist = []
for denominator in range(1, 14, 3):
    print("1/" + str(denominator)) #print 1/1
    sumserieslist.append("1/" + str(denominator))
print(sumserieslist) #print ['1/1', '1/4', '1/7', '1/10', '1/13']
sumnthterm = 1 / 1
for eachfraciton in sumserieslist[1:]:
    print(int(eachfraciton[2:])) #print 4
    nthterm = int(1) / int(eachfraciton[2:])
    print(nthterm) #print 0.25
    sumnthterm += nthterm
print(sumnthterm) #print 1.5697802197802198
print(round(sumnthterm, 2)) #print 1.57
