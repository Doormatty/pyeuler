i = 1
foo = 0
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        foo += 1
    i += 1
print(foo)