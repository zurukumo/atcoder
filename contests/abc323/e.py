N, X = map(int, input().split())
T = [int(i) for i in input().split()]

mod = 998244353
inv = pow(N, mod - 2, mod)

dp = [0] * (X + 1)
dp[0] = 1

for i in range(X + 1):
    for t in T:
        if i + t <= X:
            dp[i + t] += dp[i] * inv
            dp[i + t] %= mod

ret = 0
for i in range(X + 1):
    if i + T[0] > X:
        ret += dp[i] * inv
        ret %= mod

print(ret)
