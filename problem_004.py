candidates = []
for start in range(900, 0, -100):
    for i in range(start, 1000):
        for j in range(i, 1000):
            if str(i * j) == str(i * j)[::-1]:
                candidates.append(i * j)
    if len(candidates) > 1:
        print(max(*candidates))
        break


# slower one-liner
# print(max(*[i * j for i in range(100, 1000) for j in range(i, 1000) if str(i * j) == str(i * j)[::-1]]))
