import collections

N = int(input())
C = [input() for _ in range(N)]

nG = [[] for _ in range(N)]
rG = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if C[i][j] == "-":
            continue
        nG[i].append((j, C[i][j]))
        rG[j].append((i, C[i][j]))

queue = collections.deque([])
ret = [[float("inf")] * N for _ in range(N)]
for i in range(N):
    ret[i][i] = 0
    queue.append((0, i, i))
    for j in range(N):
        if C[i][j] != "-":
            if i != j:
                ret[i][j] = 1
                queue.append((1, i, j))

while queue:
    cost, f1, t1 = queue.popleft()
    if cost > ret[f1][t1]:
        continue

    for f2, c1 in rG[f1]:
        for t2, c2 in nG[t1]:
            if c1 != c2:
                continue
            if cost + 2 < ret[f2][t2]:
                ret[f2][t2] = cost + 2
                queue.append((cost + 2, f2, t2))

for i in range(N):
    print(*[-1 if ret[i][j] == float("inf") else ret[i][j] for j in range(N)])
