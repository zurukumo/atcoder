N, M = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(M)]
c = [int(i) for i in input().split()]

graph = [[] for _ in range(N)]
for a, b in ab:
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

groups = [-1] * N
group = 0
for i in range(N):
    if groups[i] != -1:
        continue
    stack = [i]
    groups[i] = group
    while stack:
        cur = stack.pop()
        for nex in graph[cur]:
            if groups[nex] != -1:
                continue
            if c[cur] == c[nex]:
                continue
            stack.append(nex)
            groups[nex] = group
    group += 1

ret = False
for a, b in ab:
    a -= 1
    b -= 1
    if c[a] == c[b] and groups[a] == groups[b]:
        ret |= True

print("Yes" if ret else "No")
