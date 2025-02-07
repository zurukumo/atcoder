from collections import deque

N, M = map(int, input().split())
v = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    v[A - 1].append(B - 1)


def bfs(i):
    dist = [float("inf")] * N
    pre = [-1] * N

    queue = deque([(i, 0)])
    while queue:
        cur, cost = queue.popleft()
        if dist[cur] < cost:
            continue
        for nex in v[cur]:
            if cost + 1 < dist[nex]:
                dist[nex] = cost + 1
                pre[nex] = cur
                queue.append((nex, cost + 1))

    return dist[i], pre


mi = -1
mv = float("inf")
mp = []
for i in range(N):
    m, pre = bfs(i)
    if m < mv:
        mi, mv, mp = i, m, pre

if mi >= 0:
    print(mv)
    cur = mi
    while mp[cur] != mi:
        print(cur + 1)
        cur = mp[cur]
    print(cur + 1)
else:
    print(-1)
