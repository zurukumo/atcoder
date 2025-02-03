N, K = map(int, input().split())
MOD = 10 ** 9 + 7

i = 1
n = []
while i <= N :
    j = N // i
    if i <= j :
        n.append(1)
        i += 1
    else :
        n.append(N//j-i+1)
        i = N // j + 1

M = len(n)

dp = [[0] * M for _ in range(K)]
dp[0] = n

for k in range(1, K) :
    sdp = [0] * M
    sdp[0] = dp[k-1][0]
    for i in range(1, M) :
        sdp[i] = (sdp[i-1] + dp[k-1][i]) % MOD
    for i in range(M) :
        dp[k][i] = sdp[M-i-1] * n[i] % MOD

ret = 0

for j in range(M) :
    ret += dp[K-1][j]
    ret %= MOD
    
print(ret)