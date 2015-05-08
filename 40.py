output=[]
for i in range(1,200000):
    for char in str(i):
        output.append(int(char))
print(output[0]*output[9]*output[99]*output[999]*output[9999]*output[99999]*output[999999])
