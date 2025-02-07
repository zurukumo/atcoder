from collections import deque

N, K = map(int, input().split())

v = [[] for i in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    v[a - 1].append(b - 1)
    v[b - 1].append(a - 1)

MOD = 10**9 + 7

dp = [0] * N
visited = [False] * N
queue = deque([0])

ret = 1
while queue:
    cur = queue.popleft()
    visited[cur] = True
    nvisited = 0

    for nex in v[cur]:
        if visited[nex]:
            nvisited += dp[nex] + 1
            dp[cur] += 1
            dp[nex] += 1
        else:
            queue.append(nex)

    if nvisited >= K:
        ret = 0
        break
    else:
        ret *= K - nvisited
        ret %= MOD

print(ret)
