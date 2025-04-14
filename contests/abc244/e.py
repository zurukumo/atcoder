N, M, K, S, T, X = map(int, input().split())
UV = [[int(i) for i in input().split()] for _ in range(M)]

graph = [[] for _ in range(N)]
for u, v in UV:
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

S -= 1
T -= 1
X -= 1

mod = 998244353

dp = [[[0, 0] for _ in range(N)] for _ in range(K + 1)]
dp[0][S][0] = 1

for k in range(K):
    for u in range(N):
        for v in graph[u]:
            if v == X:
                dp[k + 1][v][0] += dp[k][u][1]
                dp[k + 1][v][0] %= mod
                dp[k + 1][v][1] += dp[k][u][0]
                dp[k + 1][v][1] %= mod
            else:
                dp[k + 1][v][0] += dp[k][u][0]
                dp[k + 1][v][0] %= mod
                dp[k + 1][v][1] += dp[k][u][1]
                dp[k + 1][v][1] %= mod

print(dp[-1][T][0])
