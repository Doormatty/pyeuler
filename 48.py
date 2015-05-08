x = 0
for i in range(1, 1001):
    x += i ** i
x = str(x)
print(x[-10:])
