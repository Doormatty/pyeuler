from eulerfunctions import primefac


i = 4
a = set(primefac(i))
b = set(primefac(i - 1))
c = set(primefac(i - 2))
d = set(primefac(i - 3))
while True:
    if len(a) >= 4 and len(b) >= 4 and len(c) >= 4 and len(d) >= 4:
        print(i, i + 1, i + 2, i + 3)
    i += 1
    d = c
    c = b
    b = a
    a = set(primefac(i))