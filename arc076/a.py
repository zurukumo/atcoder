import sys

input = sys.stdin.readline

N, M = map(int, input().split())
mod = 10**9 + 7

if N < M:
    N, M = M, N

if N - M == 0:
    ret = 1
    for i in range(1, N + 1):
        ret = ret * i * i % mod
    print(ret * 2 % mod)

elif N - M == 1:
    ret = 1
    for i in range(1, M + 1):
        ret = ret * i * i % mod
    print(ret * N % mod)
else:
    print(0)
