import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M, L = map(int, input().split())
v = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    if C > L:
        continue
    v[A - 1].append((B - 1, C))
    v[B - 1].append((A - 1, C))

Q = int(input())

start = defaultdict(lambda: [])
for i in range(Q):
    s, t = map(int, input().split())
    start[s - 1].append((t - 1, i))

INF = N * N
ret = [-1] * Q
for s, d in start.items():
    # print(s, d)
    pre1 = [-1] * N
    pre2 = [INF] * N
    pre1[s] = L  # のこりのガソリン
    pre2[s] = 0  # 補充回数
    queue = deque([(s, L, 0)])

    while queue:
        # print(queue)
        cur, rest, cost = queue.popleft()
        if pre2[cur] < cost or (pre2[cur] == cost and pre1[cur] > rest):
            continue

        for nex, c in v[cur]:
            if rest >= c:
                nrest = rest - c
                ncost = cost
            else:
                nrest = L - c
                ncost = cost + 1

            if ncost < pre2[nex] or (ncost == pre2[nex] and nrest > pre1[nex]):
                queue.append((nex, nrest, ncost))
                pre1[nex] = nrest
                pre2[nex] = ncost

    # print(pre1)
    # print(pre2)
    # print()

    for dest, i in d:
        if pre1[dest] == -1:
            ret[i] = -1
        else:
            ret[i] = pre2[dest]

for r in ret:
    print(r)
