L = input()
MOD = 10 ** 9 + 7
N = len(L)

dp = [[0] * 2 for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N) :
    if L[i] == '1' :
        dp[i+1][0] = (dp[i][0] * 2) % MOD
        dp[i+1][1] = (dp[i][0] + dp[i][1] * 3) % MOD
    else :
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = (dp[i][1] * 3) % MOD

print(sum(dp[N]) % MOD)