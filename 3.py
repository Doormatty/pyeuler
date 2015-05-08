num=600851475143
for x in range (2,num//2):
    if (num%x==0):
        for y in range (2,x//2):
            if (x%y==0):
                break
        else:
            print(x, 'is prime')
            num=num/x
            prime=x
print (prime)