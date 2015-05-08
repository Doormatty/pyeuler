import time

starttime = time.time()


def check_palindrome(data, case=True, strip=True):
    bar = ascii(data)
    if strip:
        bar = bar.replace(' ', '')
    if case:
        bar = bar.upper()
    length = len(bar)
    if length % 2 == 0:
        if (bar[:(length // 2)]) == (bar[length:(length // 2 - 1):-1]):
            return True
    else:
        if (bar[:(length // 2)]) == (bar[length:(length // 2):-1]):
            return True
    return False


result = 0
for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        if (x * y) > result:  # Before we do the slow palindrome check, first do a fast check to see if this candidate is even big enough
            if check_palindrome(x * y):
                result = x * y
        else:  # If X*Y is smaller than the current result, since we're iterating downwards, this iteration of the Y loop is now useless
            break
    if (x * 999) < result:  # Same as previous sanity check
        break
print('Result :', result, '  Time:', (time.time() - starttime))
 
