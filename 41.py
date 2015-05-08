from eulerfunctions import isprime

highnum = 0
for i in range(7654321, 1234567, -1):
    l = list(str(i))
    if (len(l) == len(set(l))) and ('0' not in l and '9' not in l and '8' not in l):
        print(l)
        if isprime(i):
            highnum = i
            print('Answer:', i)
            break