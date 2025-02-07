import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
Query = [[int(i) for i in input().split()] for _ in range(Q)]

a = [N] * (N + 1)
b = [N] * (N + 1)
ret = (N - 2) * (N - 2)
H = N
W = N

for mode, x in Query:
    if mode == 1:
        for i in range(x, W + 1):
            b[i] = H
        W = min(W, x)
        ret -= b[x] - 2
    else:
        for i in range(x, H + 1):
            a[i] = W
        H = min(H, x)
        ret -= a[x] - 2

print(ret)
