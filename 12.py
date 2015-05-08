import time
from eulerfunctions import factor


def TriNum(n):
    return sum(range(1, n + 1))


starttime = time.time()
i = 12373
while True:
    print(i)
    testnum = TriNum(i)
    if testnum % 2 == 0:
        numdiv = len(factor(testnum))
        if numdiv > 500:
            break
    i += 1
print(i, 'th Triangle # is: ', TriNum(i))
print('Time :', time.time() - starttime)
