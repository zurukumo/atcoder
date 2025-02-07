N, D = map(int, input().split())
X = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
for i in range(N):
    for j in range(i + 1, N):
        d = 0
        for k in range(D):
            d += (X[i][k] - X[j][k]) ** 2

        k = 1
        while k * k < d:
            k += 1
        if k * k == d:
            ret += 1

print(ret)
