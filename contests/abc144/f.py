import sys

input = sys.stdin.readline

N, M = map(int, input().split())
v = [[] for _ in range(N)]
for i in range(M):
    s, t = map(int, input().split())
    v[s - 1].append(t - 1)

# 削除しないでdp
dp = [0] * N
for i in range(N - 1, -1, -1):
    if len(v[i]) == 0:
        continue

    for j in v[i]:
        dp[i] += dp[j]
    dp[i] = 1 + dp[i] / len(v[i])

ret = dp[0]
# 削除してdp
for i in range(N - 1):
    if len(v[i]) <= 1:
        continue

    dp[i] = 0
    M = -1
    for j in v[i]:
        dp[i] += dp[j]
        M = max(M, dp[j])
    dp[i] = 1 + (dp[i] - M) / (len(v[i]) - 1)

    for j in range(i - 1, -1, -1):
        if len(v[j]) == 0:
            continue

        dp[j] = 0
        for k in v[j]:
            dp[j] += dp[k]
        dp[j] = 1 + dp[j] / len(v[j])

    ret = min(ret, dp[0])

print(ret)
