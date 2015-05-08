def check_palindrome (input,case=True,strip=True):
    bar=ascii(input)
    if (strip):
        bar=bar.replace(' ', '')
    if (case):
        bar=bar.upper()
    length=len(bar)
    if (length%2==0):
        if ((bar[:(length//2)])==(bar[length:(length//2-1):-1])):
            return True
    else:
        if ((bar[:(length//2)])==(bar[length:(length//2):-1])):
            return True
    return False

def IsLychrel(x,r=0):
    if r>=50:
        return True
    print ('Recursed',r,'times')
    print ('Starting with',x)
    print ('Adding',str(x)[::-1])
    x=x+int(str(x)[::-1])
    print ('To get',x)
    
    if not check_palindrome(str(x)):
        print ('Is not a palindrome')
        return IsLychrel(x,r+1)
    else:
        print ('Is Palindromic')
        return False

num=0
for i in range(1,10001):
    if IsLychrel(i):
        num=num+1
        
print (num)