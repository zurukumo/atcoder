from heapq import heappop, heappush

N, M, T = map(int, input().split())
A = [int(i) for i in input().split()]

v1 = [[] for _ in range(N)]
v2 = [[] for _ in range(N)]
w1 = [float("inf")] * N
w2 = [float("inf")] * N

for _ in range(M):
    a, b, c = map(int, input().split())
    v1[a - 1].append((b - 1, c))
    v2[b - 1].append((a - 1, c))

# 0->各点への最短距離を求める
queue = [(0, 0)]
while queue:
    cost1, cur = heappop(queue)
    if cost1 > w1[cur]:
        continue

    for nex, cost2 in v1[cur]:
        if w1[nex] > cost1 + cost2:
            w1[nex] = cost1 + cost2
            if nex != 0:
                heappush(queue, (cost1 + cost2, nex))

# 各点->0への最短距離を求める
queue = [(0, 0)]
while queue:
    cost1, cur = heappop(queue)
    if cost1 > w2[cur]:
        continue

    for nex, cost2 in v2[cur]:
        if w2[nex] > cost1 + cost2:
            w2[nex] = cost1 + cost2
            if nex != 0:
                heappush(queue, (cost1 + cost2, nex))

ret = A[0] * T
for i in range(1, N):
    ret = max(ret, (T - w1[i] - w2[i]) * A[i])

print(ret)
