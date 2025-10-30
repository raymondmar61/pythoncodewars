#https://www.codewars.com/kata/563f037412e5ada593000114/train/python
'''
Money, Money, Money 7kyu

Mr. Scrooge has a sum of money 'P' that he wants to invest. Before he does, he wants to know how many years 'Y' this sum 'P' has to be kept in the bank in order for it to amount to a desired sum of money 'D'.

The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly. After paying taxes 'T' for the year the new sum is re-invested.

Note to Tax: not the invested principal is taxed, but only the year's accrued interest

Example:

  Let P be the Principal = 1000.00
  Let I be the Interest Rate = 0.05
  Let T be the Tax Rate = 0.18
  Let D be the Desired Sum = 1100.00

After 1st Year -->  P = 1041.00
After 2nd Year -->  P = 1083.86
After 3rd Year -->  P = 1128.30

Thus Mr. Scrooge has to wait for 3 years for the initial principal to amount to the desired sum.

Your task is to complete the method provided and return the number of years 'Y' as a whole in order for Mr. Scrooge to get the desired sum.

Assumption: Assume that Desired Principal 'D' is always greater than the initial principal. However it is best to take into consideration that if Desired Principal 'D' is equal to Principal 'P' this should return 0 Years.
'''
def calculate_years(principal, interest, tax, desired):
    if principal == desired:
        return 0
    import itertools
    for year in itertools.count(1):
        if year == 1:
            interestearned = round(principal * interest, 2)
            endofyear = round(principal + interestearned, 2)
            endofyeartaxpaid = round(interestearned * tax, 2)
            endofyearfinal = round(endofyear - endofyeartaxpaid, 2)
        else:
            interestearned = round(endofyearfinal * interest, 2)
            endofyear = round(endofyearfinal + interestearned, 2)
            endofyeartaxpaid = round(interestearned * tax, 2)
            endofyearfinal = round(endofyear - endofyeartaxpaid, 2)
        if endofyearfinal >= desired:
            return year


print(calculate_years(1000.00, 0.05, 0.18, 1100.00))
print(calculate_years(1000.00, 0.01625, 0.18, 1200))
print(calculate_years(1000.00, 0.05, 0.18, 1000))


principal = 1000.00
interestrate = 0.05
taxrate = 0.18
desiredsum = 1100.00

interestearned = round(principal * interestrate, 2)
endofyear = round(principal + interestearned, 2)
endofyeartaxpaid = round(interestearned * taxrate, 2)
endofyearfinal = round(endofyear - endofyeartaxpaid, 2)

print(interestearned)
print(endofyear)
print(endofyeartaxpaid)
print(endofyearfinal)
print("\n")

interestearned = round(endofyearfinal * interestrate, 2)
endofyear = round(endofyearfinal + interestearned, 2)
endofyeartaxpaid = round(interestearned * taxrate, 2)
endofyearfinal = round(endofyear - endofyeartaxpaid, 2)

print(interestearned)
print(endofyear)
print(endofyeartaxpaid)
print(endofyearfinal)
print("\n")

interestearned = round(endofyearfinal * interestrate, 2)
endofyear = round(endofyearfinal + interestearned, 2)
endofyeartaxpaid = round(interestearned * taxrate, 2)
endofyearfinal = round(endofyear - endofyeartaxpaid, 2)

print(interestearned)
print(endofyear)
print(endofyeartaxpaid)
print(endofyearfinal)

principal = 1000.00
interestrate = 0.05
taxrate = 0.18
desiredsum = 1100.00

for year in range(1, 100):
    print(year)
    if year == 1:
        interestearned = round(principal * interestrate, 2)
        endofyear = round(principal + interestearned, 2)
        endofyeartaxpaid = round(interestearned * taxrate, 2)
        endofyearfinal = round(endofyear - endofyeartaxpaid, 2)
    else:
        interestearned = round(endofyearfinal * interestrate, 2)
        endofyear = round(endofyearfinal + interestearned, 2)
        endofyeartaxpaid = round(interestearned * taxrate, 2)
        endofyearfinal = round(endofyear - endofyeartaxpaid, 2)
    print(interestearned)
    print(endofyear)
    print(endofyeartaxpaid)
    print(endofyearfinal)
    if endofyearfinal >= desiredsum:
        print(year)
        break
