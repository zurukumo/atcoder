N, M, K = map(int, input().split())
ABC = [[int(i) for i in input().split()] for _ in range(M)]
E = [int(i) for i in input().split()]

cost = [float("inf")] * N
cost[0] = 0
for e in E:
    e -= 1
    a, b, c = ABC[e]
    a -= 1
    b -= 1
    cost[b] = min(cost[b], cost[a] + c)

if cost[-1] == float("inf"):
    print(-1)
else:
    print(cost[-1])
