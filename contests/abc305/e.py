import heapq

N, M, K = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(M)]
ph = [[int(i) for i in input().split()] for _ in range(K)]

graph = [[] for _ in range(N)]
for a, b in ab:
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


hq = []
cost = [-1] * N
for p, h in ph:
    p -= 1
    heapq.heappush(hq, (-h, p))
    cost[p] = h

while hq:
    hp, cur = heapq.heappop(hq)
    hp = -hp
    if hp < cost[cur]:
        continue
    for nex in graph[cur]:
        if hp - 1 <= cost[nex]:
            continue
        heapq.heappush(hq, (-(hp - 1), nex))
        cost[nex] = hp - 1

ret = []
for i in range(N):
    if cost[i] >= 0:
        ret.append(i + 1)

print(len(ret))
print(*ret)
