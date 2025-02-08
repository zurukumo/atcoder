from heapq import heappop, heappush

N = int(input())
a, b = map(int, input().split())
M = int(input())
INF = 10**10
MOD = 10**9 + 7

v = [[] for _ in range(N + 1)]
w = [INF] * (N + 1)
n = [0] * (N + 1)
n[0] = 1

for _ in range(M):
    x, y = map(int, input().split())
    v[x].append(y)
    v[y].append(x)

queue = [(0, a, 0)]

while queue:
    cost, current, prev = heappop(queue)
    if w[current] < cost:
        continue

    if w[current] != cost:
        for next in v[current]:
            heappush(queue, (cost + 1, next, current))

    n[current] = (n[current] + n[prev]) % MOD
    w[current] = cost

print(n[b])
