N, M = map(int, input().split())
a = [True] * (N + 3)
a[N + 1] = False
a[N + 2] = False

for _ in range(M) :
    a[int(input())] = False

MOD = 10 ** 9 + 7

dp = [0] * (N + 3)
dp[0] = 1
for i in range(N) :
    if a[i + 1] :
        dp[i + 1] = (dp[i + 1] + dp[i]) % MOD
    if a[i + 2] :
        dp[i + 2] = (dp[i + 2] + dp[i]) % MOD
   
print(dp[N])