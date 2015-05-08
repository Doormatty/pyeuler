falseset = {1}
trueset = {89}


def schain(x):
    # print ('Checking',x,'.')
    tset = set()
    global falseset
    global trueset
    while True:
        #print (x,'->',end='')
        if x in trueset or x == 89:
            #print ('is in true cache.')
            for num in tset:
                trueset.add(num)
            return True
        elif x in falseset or x == 1:
            #print ('is in False cache.')
            for num in tset:
                falseset.add(num)
            return False
        tset.add(x)
        t = 0
        for i in str(x):
            t += int(i) ** 2
        x = t


runsum = 0
for i in range(2, 10000000):
    if i % 10000 == 0:
        print('#', i)
    schain(i)
print(runsum)