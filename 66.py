import math
from fractions import Fraction

# x is the value of d  in x^2-dy^2=1, and y is the how many times to recurse through the values. 
# it will output a tuple of num,dom.  Increase the value of y until num=x and dom=y are valid answers.

def pell(x, y):
    xsqr = math.sqrt(x)
    if int(xsqr) == xsqr:
        return 0
    olist = [(0, 1, math.floor(xsqr))]
    i = 0
    for foo in range(y):
        i += 1
        m = int(olist[i - 1][1] * olist[i - 1][2] - olist[i - 1][0])
        d = int((x - m ** 2) / olist[i - 1][1])
        a = math.floor((olist[0][2] + m) / d)
        olist.append((m, d, a))

    elist = [i[2] for i in olist]

    runsum = Fraction(0)

    for i in range(len(elist) - 1, -1, -1):
        if i == len(elist) - 1:
            c = elist[i]
        else:
            c = elist[i] + (1 / runsum)
        runsum = Fraction(c)
    return runsum.numerator, runsum.denominator


high = 0
highnum = 0

for d in range(1, 1001):
    x = math.sqrt(d)
    if int(x) == x:
        continue
    i = 0
    while True:
        foo = pell(d, i)
        if (foo[0] ** 2 - d * foo[1] ** 2) == 1:
            print(d, ':', foo[0])
            if foo[0] > high:
                high = foo[0]
                highnum = d
            break
        else:
            i += 1

print('High d is', highnum, 'with a x of', high)