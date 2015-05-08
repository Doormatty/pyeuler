def check_palindrome(input, case=True, strip=True):
    bar = str(input)
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


def baseN(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and "0" ) or ( baseN(num // b, b).lstrip("0") + numerals[num % b])


runsum = 0
for i in range(1, 1000000):
    if check_palindrome(i) and check_palindrome(baseN(i, 2)):
        runsum += i
print(runsum)