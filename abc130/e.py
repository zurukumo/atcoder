N, M = map(int, input().split())
S = [int(i) for i in input().split()]+['g']
T = [int(i) for i in input().split()]+['a']

MOD = 10 ** 9 + 7

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N + 1) :
    dp[i][0] = 1
for i in range(M + 1) :
    dp[0][i] = 1

for i in range(1, N + 1) :
    for j in range(1, M + 1) :
        
        if S[i-1] == T[j-1] :
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
        else :
            dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]) % MOD

print(dp[N][M])