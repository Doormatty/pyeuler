i=20
flag=True
while True:
    for x in range(19,1,-1):
        if (i % x != 0):
            flag=False
            break
    if (flag):
        break
    else:
        flag=True
    i+=20
print (i)
