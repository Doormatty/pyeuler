import time

starttime = time.time()
y = 2
data = 0
for i in range(0, 999):
    y *= 2
print(y)

numbers = str(y)
for i in range(0, len(numbers)):
    data += int(numbers[i:i + 1])
print(data)
print('Time:', time.time() - starttime)