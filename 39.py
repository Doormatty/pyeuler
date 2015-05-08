output = [0] * 1001
for c in range(1, 1000):
    cc = c * c
    for a in range(1, c):
        if c + a > 999: break
        aa = a * a
        for b in range(1, c):
            if c + a + b > 999: break
            bb = b * b
            if cc - (aa + bb) == 0:
                output[a + b + c] += 1
print(output.index(max(output)))
                
                