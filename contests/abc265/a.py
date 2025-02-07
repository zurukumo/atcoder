X, Y, N = map(int, input().split())

ret = float("inf")
for i in range(N + 1):
    for j in range(N + 1):
        if i + 3 * j == N:
            ret = min(ret, X * i + Y * j)
print(ret)
