A, B = map(int, input().split())

ret = -float("inf")
for a in range(100, 1000):
    for b in range(100, 1000):
        ca, cb = 0, 0
        for i, j in zip(str(A), str(a)):
            if i != j:
                ca += 1
        for i, j in zip(str(B), str(b)):
            if i != j:
                cb += 1
        if ca + cb <= 1:
            ret = max(ret, a - b)

print(ret)
