from itertools import permutations, product

N, M = map(int, input().split())
UVT = [[int(i) for i in input().split()] for _ in range(M)]
Q = int(input())

cost = [[float("inf")] * N for _ in range(N)]
for u, v, t in UVT:
    cost[u - 1][v - 1] = min(cost[u - 1][v - 1], t)
    cost[v - 1][u - 1] = min(cost[v - 1][u - 1], t)
for i in range(N):
    cost[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for _ in range(Q):
    K = int(input())
    B = [int(i) for i in input().split()]
    selected_uvt = [UVT[b - 1] for b in B]

    ret = float("inf")
    for uvt in permutations(selected_uvt):
        for switch_list in product(range(2), repeat=K):
            tmp = 0
            cur = 0
            for (u, v, t), switch in zip(uvt, switch_list):
                if switch == 0:
                    tmp += cost[cur][u - 1]
                    tmp += t
                    cur = v - 1
                else:
                    tmp += cost[cur][v - 1]
                    tmp += t
                    cur = u - 1
            tmp += cost[cur][N - 1]
            ret = min(ret, tmp)
    print(ret)
