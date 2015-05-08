import time

abun = []
f = open('23abundant.txt', 'r')
for line in f:
    abun.append(int(line))
f.close()
starttime = time.time()
abunsum = {a + b for a in abun for b in abun if (a + b < 20164)}
notabunsum = [a for a in range(1, 20164) if a not in abunsum]
print(sum(notabunsum))
print('Time:', time.time() - starttime)
