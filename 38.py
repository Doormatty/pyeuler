highnum = 0
for i in range(1, 10000):
    temp = ''
    for x in range(1, 10):
        temp += str(i * x)
        if len(set(temp)) == 9 and len(temp) == 9 and not '0' in set(temp):
            if int(temp) > highnum: highnum = int(temp)
print(highnum)
            