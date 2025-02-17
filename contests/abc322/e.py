import collections
import itertools

N, K, P = map(int, input().split())
CA = [[int(i) for i in input().split()] for _ in range(N)]

cost = collections.defaultdict(lambda: float("inf"))
cost[tuple([0] * K)] = 0

for c, *a in CA:
    for cur in itertools.product(range(P, -1, -1), repeat=K):
        nex = list(cur)
        for i in range(K):
            nex[i] += a[i]
            nex[i] = min(nex[i], P)
        nex = tuple(nex)
        cost[nex] = min(cost[nex], cost[cur] + c)

if cost[tuple([P] * K)] != float("inf"):
    print(cost[tuple([P] * K)])
else:
    print(-1)
