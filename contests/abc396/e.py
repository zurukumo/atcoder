N, M = map(int, input().split())
XYZ = [[int(i) for i in input().split()] for _ in range(M)]

cost = [-1] * N
graph = [[] for _ in range(N)]
for x, y, z in XYZ:
    x -= 1
    y -= 1
    graph[x].append((y, z))
    graph[y].append((x, z))

for i in range(N):
    if cost[i] != -1:
        continue

    cost[i] = 0
    cnt = 1
    bit_cnt = [0] * 31
    stack = [i]
    while stack:
        cur = stack.pop()
        for nex, c in graph[cur]:
            if cost[nex] != -1:
                if cost[nex] != (cost[cur] ^ c):
                    print(-1)
                    exit()
                else:
                    continue

            cost[nex] = cost[cur] ^ c
            cnt += 1
            for j in range(31):
                if cost[nex] & (1 << j):
                    bit_cnt[j] += 1
            stack.append(nex)

    visited = set()
    stack = [i]
    visited.add(i)
    for j in range(31):
        if cnt - bit_cnt[j] < bit_cnt[j]:
            cost[i] ^= 1 << j
    while stack:
        cur = stack.pop()
        for nex, c in graph[cur]:
            if nex in visited:
                continue

            stack.append(nex)
            visited.add(nex)
            for j in range(31):
                if cnt - bit_cnt[j] < bit_cnt[j]:
                    cost[nex] ^= 1 << j

print(*cost)
