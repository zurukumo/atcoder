N, C = map(int, input().split())
A = [int(i) for i in input().split()]

dp = [0] * N
for i in range(N):
    dp[i] += A[i]
    if i > 0:
        dp[i] += dp[i - 1]

diff = 0
m = 0
M = 0
for i in range(N):
    diff = max(diff, (dp[i] - m) * (C - 1), (dp[i] - M) * (C - 1))
    m = min(m, dp[i])
    M = max(M, dp[i])

print(sum(A) + diff)
