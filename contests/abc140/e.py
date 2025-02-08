from heapq import heappop, heappush

N = int(input())
P = [int(i) for i in input().split()]

dpl = [[] for _ in range(N)]
dpr = [[] for _ in range(N)]
q = []
for i in range(N - 1, -1, -1):
    L = []
    while len(q) > 0 and q[0][0] < P[i]:
        v, j = heappop(q)
        if len(dpl[j]) == 0:
            L.append([v, j])
        dpl[j].append(i)
    for v, j in L:
        heappush(q, [v, j])
    heappush(q, [P[i], i])

q = []
for i in range(N):
    L = []
    while len(q) > 0 and q[0][0] < P[i]:
        v, j = heappop(q)
        if len(dpr[j]) == 0:
            L.append([v, j])
        dpr[j].append(i)
    for v, j in L:
        heappush(q, [v, j])
    heappush(q, [P[i], i])

for i in range(N):
    for _ in range(2 - len(dpl[i])):
        dpl[i].append(-1)
    for _ in range(2 - len(dpr[i])):
        dpr[i].append(N)
    dpl[i].sort()
    dpr[i].sort()

ret = 0
for i in range(N):
    ret += (dpl[i][1] - dpl[i][0]) * (dpr[i][0] - i) * P[i]
    ret += (i - dpl[i][1]) * (dpr[i][1] - dpr[i][0]) * P[i]

print(ret)
