def digitalsum(x):
    y = 0
    for i in str(x):
        y += int(i)
    return y


runsum = 0
for x in range(0, 101):
    for y in range(0, 101):
        foo = digitalsum(x ** y)
        if foo > runsum:
            runsum = foo

print(runsum)