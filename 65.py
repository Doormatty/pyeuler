from fractions import Fraction


def egen():
    yield 2
    yield 1
    i = 0
    while True:
        i += 1
        yield 2 * i
        yield 1
        yield 1


def efrac(x):
    runsum = Fraction(0)
    e = egen()
    elist = []
    for i in range(x):
        elist.append(next(e))
    for i in range(len(elist) - 1, -1, -1):
        if i == len(elist) - 1:
            c = elist[i]
            # print (i,': Bottom: runsum=',elist[i],sep='')
        else:
            c = elist[i] + (1 / runsum)
            # print (i,': runsum=',elist[i],'+(',runsum,'/',1,')=',c,sep='')
        runsum = Fraction(c)
    return runsum


x = str(efrac(100).numerator)
runsum = 0
for char in x:
    runsum += int(char)
print(runsum)
