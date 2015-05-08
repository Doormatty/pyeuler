def fib():
    a,b=1,1
    yield 1
    yield 1
    while True:
        yield a+b
        a,b=b,a+b

i=0
foo=fib()
while True:
    i+=1
    if len(str(next(foo)))==1000:
        break
print (i)

