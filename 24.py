import itertools
import time

combo = itertools.permutations('0123456789')

starttime = time.time()
i = 0
for x in combo:
    i += 1
    if i == 1000000:
        print('1000000:', x)
        break
print('Time', time.time() - starttime)