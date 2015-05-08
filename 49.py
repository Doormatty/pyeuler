from eulerfunctions import isprime


for x in range(1000, 3334):
    if isprime(x):
        for y in range(1000, 3334):
            if set(str(x)) == set(str(y + x)) and isprime(x + y):
                if set(str(x)) == set(str(y + y + x)) and isprime(x + y + y):
                    print(x, y + x, y + y + x)