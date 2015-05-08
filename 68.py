import itertools

olist = []
oolist = []
x = itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for c in x:
    t = [int(i) for i in list(c)]
    if (t[0] + t[1] + t[2]) == (t[3] + t[2] + t[4]) == (t[5] + t[4] + t[6]) == (t[7] + t[6] + t[8]) == (
            t[9] + t[8] + t[1]):
        olist.append(
            [[t[0], t[1], t[2]], [t[3], t[2], t[4]], [t[5], t[4], t[6]], [t[7], t[6], t[8]], [t[9], t[8], t[1]]])

for x in olist:
    start = [i[0] for i in x].index(min([i[0] for i in x]))
    # print (x,'start with',start)
    runsum = ''
    for foo in range(start, start + 5):
        runsum += str(x[foo % 5][0]) + str(x[foo % 5][1]) + str(x[foo % 5][2])
    oolist.append(int(runsum))
oolist = [i for i in oolist if len(str(i)) == 16]
print(max(oolist))