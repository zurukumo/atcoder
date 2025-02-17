import collections

M = int(input())
uv = [[int(i) for i in input().split()] for _ in range(M)]
p = [int(i) for i in input().split()]

set_uv = set()
for u, v in uv:
    u -= 1
    v -= 1
    set_uv.add((min(u, v), max(u, v)))

init = [-1] * 9
for i, p in enumerate(p):
    init[p - 1] = i

queue = collections.deque([tuple(init)])
cost = dict()
cost[tuple(init)] = 0
while queue:
    now = queue.popleft()
    for i in range(9):
        for j in range(i + 1, 9):
            if (now[i] == -1 or now[j] == -1) and (i, j) in set_uv:
                next = list(now)
                next[i], next[j] = next[j], next[i]
                next = tuple(next)
                if next not in cost:
                    cost[next] = cost[now] + 1
                    queue.append(next)

if (0, 1, 2, 3, 4, 5, 6, 7, -1) in cost:
    print(cost[(0, 1, 2, 3, 4, 5, 6, 7, -1)])
else:
    print(-1)
