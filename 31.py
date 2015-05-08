foo = 1  # Starts at one, due to the fact that we can use a 2 pound coin only one way.
for a in range(0, 3):
    for b in range(0, 5 - a * 2):
        for c in range(0, 11 - a * 5):
            for d in range(0, 21 - (a * 10 + b * 5 + c * 2)):
                for e in range(0, 41 - (a * 20 + b * 10 + c * 4 + d * 2)):
                    for f in range(0, 101 - (a * 50 + c * 10 + d * 5)):
                        for g in range(0, 201 - (a * 100 + b * 50 + c * 20 + d * 10 + e * 5 + f * 2)):
                            if a * 100 + b * 50 + c * 20 + d * 10 + e * 5 + f * 2 + g == 200:
                                foo += 1
print(foo)