data = 0
f = open('13input.txt', 'r')
for line in f:
    data += int(line)
f.close()
s = str(data)
print(s[0:10])

