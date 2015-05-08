from eulerfunctions import ishexa, ispenta, trigen


d = trigen()
n = 0
for i in d:
    n += 1
    if ishexa(i) and ispenta(i):
        print(n, '->', i)