t = []
# Reads an arbatrary sized triangle into an list
lines = 0
f = open('67input.txt', 'r')
for line in f:
    t.append([int(i) for i in line[:-1].split()])
f.close

for y in range(len(t) - 2, -1, -1):
    for x in range(len(t[y])):
        t[y][x] += max(t[y + 1][x], t[y + 1][x + 1])

print(t[0][0])