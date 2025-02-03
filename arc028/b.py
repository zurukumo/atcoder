from heapq import heappush, heappop

N, K = map(int, input().split())
X = [int(i) for i in input().split()]

h = []
for i in range(N):
    heappush(h, (-X[i], i))

    if len(h) > K:
        heappop(h)

    if len(h) == K:
        print(h[0][1] + 1)
