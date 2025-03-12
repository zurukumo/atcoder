import heapq

N, M = map(int, input().split())
H = [int(i) for i in input().split()]
UV = [[int(i) for i in input().split()] for _ in range(M)]


def cost(x, y):
    if x >= y:
        return 0
    else:
        return y - x


graph = [[] for _ in range(N)]
for u, v in UV:
    u -= 1
    v -= 1
    graph[u].append((v, cost(H[u], H[v])))
    graph[v].append((u, cost(H[v], H[u])))

dp = [float("inf")] * N
dp[0] = 0
queue = [(0, 0)]
while queue:
    cc, cur = heapq.heappop(queue)
    if cc > dp[cur]:
        continue

    for nex, c in graph[cur]:
        if cc + c < dp[nex]:
            dp[nex] = cc + c
            heapq.heappush(queue, (dp[nex], nex))

print(max(max(0, H[0] - H[i]) - dp[i] for i in range(N)))
