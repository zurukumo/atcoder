from collections import Counter

N = int(input())
T = [int(input()) for _ in range(N)]

T.sort()

penalty = 0
for i in range(N):
    penalty += T[i] * (N - i)

mod = 10**9 + 7
fac = [1]
for i in range(1, N + 1):
    fac.append(fac[-1] * i % mod)

way = 1
for i in Counter(T).values():
    way *= fac[i]
    way %= mod

print(penalty)
print(way)
