from heapq import heappop, heappush

N, M = map(int, input().split())
AB = [[] for _ in range(M + 1)]

for _ in range(N):
    a, b = map(int, input().split())
    if a <= M:
        AB[M - a].append(b)

q = []
for a in range(M + 1):
    for b in AB[a]:
        heappush(q, b)
        if len(q) > a + 1:
            heappop(q)

print(sum(q))
