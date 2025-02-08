from heapq import heappop, heappush

N, M = map(int, input().split())
vec = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    vec[A - 1].append(B - 1)
    vec[B - 1].append(A - 1)

q = [(0, 0)]
dist = [float("inf")] * N
dist[0] = 0
ret = [-1] * N
ret[0] = 0

while q:
    cc, cur = heappop(q)
    for nex in vec[cur]:
        if cc + 1 < dist[nex]:
            dist[nex] = cc + 1
            ret[nex] = cur
            heappush(q, (cc + 1, nex))

if -1 in ret:
    print("No")
else:
    print("Yes")
    for i in range(1, N):
        print(ret[i] + 1)
