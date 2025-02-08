from bisect import bisect_right

N = int(input())
D = [-float("inf")] + [int(input()) for _ in range(N)] + [float("inf")]
mod = 10**9 + 7

D.sort()
s = list(range(N + 2))

for _ in range(3):
    t = [0] * (N + 2)
    for i in range(1, N + 1):
        t[i] = s[bisect_right(D, D[i] // 2) - 1]
    for i in range(1, N + 1):
        t[i] += t[i - 1]
        t[i] %= mod
    s = t

print(s[-2])
