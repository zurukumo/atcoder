import collections

N = int(input())
A = [int(i) for i in input().split()]

mod = 998244353
ret = [0] * (N + 1)

for i in range(N):
    for j in range(i + 1, N):
        diff = A[j] - A[i]
        if diff == 0:
            continue

        dp = collections.defaultdict(int)
        dp[A[i]] = dp[A[j]] = 1

        for k in range(j + 1, N):
            if A[k] == A[i] or A[k] == A[j]:
                continue
            dp[A[k]] += dp[A[k] - diff]

        for key, value in dp.items():
            if key == A[i] or key == A[j] or value == 0:
                continue
            ret[(key - A[i]) // diff + 1] += value
            ret[(key - A[i]) // diff + 1] %= mod


fac = [1]
for i in range(1, N + 1):
    fac.append(fac[-1] * i % mod)
inv = [1] * (N + 1)
inv[N] = pow(fac[N], mod - 2, mod)
for i in range(N - 1, 0, -1):
    inv[i] = inv[i + 1] * (i + 1) % mod


counter = collections.Counter(A)
for value in counter.values():
    for i in range(1, value + 1):
        ret[i] += fac[value] * inv[i] * inv[value - i]
        ret[i] %= mod

ret[1] = N
if N > 1:
    ret[2] = N * (N - 1) // 2

print(*ret[1:])
