#https://www.codewars.com/kata/56530b444e831334c0000020/train/python
'''
Determine offspring sex based on genes XX and XY chromosomes  8kyu

The male gametes or sperm cells in humans and other mammals are heterogametic and contain one of two types of sex chromosomes. They are either X or Y. The female gametes or eggs however, contain only the X sex chromosome and are homogametic.

The sperm cell determines the sex of an individual in this case. If a sperm cell containing an X chromosome fertilizes an egg, the resulting zygote will be XX or female. If the sperm cell contains a Y chromosome, then the resulting zygote will be XY or male.

Determine if the sex of the offspring will be male or female based on the X or Y chromosome present in the male's sperm.

If the sperm contains the X chromosome, return "Congratulations! You're going to have a daughter."; If the sperm contains the Y chromosome, return "Congratulations! You're going to have a son.";
'''
def chromosome_check(chromosome):
    chromosome = chromosome.upper()
    return "Congratulations! You\'re going to have a son." if "Y" in chromosome else "Congratulations! You\'re going to have a daughter."


print(chromosome_check('XY')) #print Congratulations! You're going to have a son.
print(chromosome_check('XX')) #print Congratulations! You're going to have a daughter.
print(chromosome_check('xy')) #print Congratulations! You're going to have a son.
print(chromosome_check('xX')) #print Congratulations! You're going to have a daughter.

if "Y" in "XY":
    print("love") #print "love"

#User submission
def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')
