N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

dp = [1] * N
for i in range(1, N):
    if A[i] > A[i - 1]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = 1

ret = 0
for i in range(N):
    if dp[i] >= K:
        ret += 1

print(ret)
