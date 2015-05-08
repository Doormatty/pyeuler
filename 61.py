# Returns a triangular number generator
def trigen():
    i = 1
    n = 0
    while True:
        n += i
        yield n
        i += 1


#Returns a square number generator
def squaregen():
    i = 1
    while True:
        yield i ** 2
        i += 1


#returns a pentagonal number generator
def pentagen():
    i = 1
    while True:
        yield int(i / 2 * (3 * i - 1))
        i += 1


#returns a hexagonal number generator
def hexagen():
    i = 1
    while True:
        yield i * (2 * i - 1)
        i += 1


#returns a heptagonal number generator
def heptagen():
    i = 1
    while True:
        yield int(i * (5 * i - 3) / 2)
        i += 1


#returns an octagonal number generator
def octagen():
    i = 1
    while True:
        yield i * (3 * i - 2)
        i += 1


trilist = []
squarelist = []
pentalist = []
hexalist = []
heptalist = []
octalist = []

a = trigen()

olist = []

while True:
    x = next(a)
    if x > 1000 and x < 9999 and str(x).find('0') == -1:
        trilist.append(x)
        olist.append([x, '3'])
    if x > 9999:
        break

a = squaregen()
while True:
    x = next(a)
    if x > 1000 and x < 9999 and str(x).find('0') == -1:
        squarelist.append(x)
        olist.append([x, '4'])
    if x > 9999:
        break

a = pentagen()
while True:
    x = next(a)
    if x > 1000 and x < 9999 and str(x).find('0') == -1:
        pentalist.append(x)
        olist.append([x, '5'])
    if x > 9999:
        break

a = hexagen()
while True:
    x = next(a)
    if x > 1000 and x < 9999 and str(x).find('0') == -1:
        hexalist.append(x)
        olist.append([x, '6'])
    if x > 9999:
        break

a = heptagen()
while True:
    x = next(a)
    if x > 1000 and x < 9999 and str(x).find('0') == -1:
        heptalist.append(x)
        olist.append([x, '7'])
    if x > 9999:
        break

a = octagen()
while True:
    x = next(a)
    if x > 1000 and x < 9999 and str(x).find('0') == -1:
        octalist.append(x)
        olist.append([x, '8'])
    if x > 9999:
        break

oolist = []
for i in trilist:
    for f in olist:
        if f[1] != '3' and str(i)[2:] == str(f[0])[:2]:
            oolist.append([[i, '3'], f])

for foo in range(3, 7):
    temp = []
    for chain in oolist:
        for i in olist:
            addflag = True
            for x in range(len(chain)):
                if chain[x][1] == i[1]:
                    addflag = False
            if str(chain[foo - 2][0])[2:] != str(i[0])[:2]:
                addflag = False
            if foo == 6:
                if str(chain[0][0])[:2] != str(i[0])[2:]:
                    addflag = False
            if addflag == True:
                temp.append(chain + [i])

    oolist = [i for i in temp if len(i) == foo]
print(oolist[0])

