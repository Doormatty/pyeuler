import itertools

f = open('59input.txt', 'r')
cipher = f.readline()
f.close()
cipher = cipher[:-1].split(',')
cipher = [int(char) for char in cipher]

output = []

password = itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=3)

# for char in cipher:
#    print(chr(char),sep="",end="")

runsum = 0
for i in password:
    x = []
    #print (i)
    for f in i:
        #print (f)
        x.append(ord(f))
    output = []
    for i in range(len(cipher)):
        output.append(cipher[i] ^ x[i % 3])
    output = [chr(char) for char in output]
    outputstr = ''.join(output)
    if outputstr.find(' the ') > 0:
        print('Password:', x)
        for char in output:
            runsum += ord(char)
        print('Sum', runsum)
        print('Plaintext:')
        for char in output:
            print(char, sep="", end="")
        
        