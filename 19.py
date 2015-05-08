def isleap(y):
    if y % 4 == 0 and not (y % 100 == 0 and not y % 400 == 0):
        return True
    else:
        return False


def dayofweek(d, m, y):
    # Sun=0 -> Sat=6
    century = 2 * (3 - (int(str(y)[0:2]) % 4))
    year = int(str(y)[2:])
    year += year // 4
    if m == 1 and isleap(y):
        month = 6
    elif m == 1 and not isleap(y):
        month = 0
    elif m == 2 and isleap(y):
        month = 2
    elif m == 2 and not isleap(y):
        month = 3
    elif m == 3:
        month = 3
    elif m == 4:
        month = 6
    elif m == 5:
        month = 1
    elif m == 6:
        month = 4
    elif m == 7:
        month = 6
    elif m == 8:
        month = 2
    elif m == 9:
        month = 5
    elif m == 10:
        month = 0
    elif m == 11:
        month = 3
    elif m == 12:
        month = 5
    return (century + year + month + d) % 7


counter = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        if dayofweek(1, m, y) == 0: counter += 1
print(counter)