output = set()
for a in range(1, 9877):
    for b in range(1, 9877):
        c = a * b
        if len(str(a) + str(b) + str(c)) == 9:
            if not c in output:
                foo = set(str(a) + str(b) + str(c))
                if len(foo) == 9 and (not '0' in foo):
                    output.add(c)
        elif len(str(a) + str(b) + str(c)) > 9:
            break
print(sum(output))