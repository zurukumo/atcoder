import itertools

N, M, K = map(int, input().split())
uvw = [[int(i) for i in input().split()] for _ in range(M)]

ret = float("inf")
for comb in itertools.combinations(range(M), N - 1):
    s = 0
    vec = [[] for _ in range(N)]
    for i in comb:
        u, v, w = uvw[i]
        u -= 1
        v -= 1
        vec[u].append(v)
        vec[v].append(u)
        s += w

    queue = [0]
    visited = set([0])
    while queue:
        cur = queue.pop()
        for nex in vec[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            queue.append(nex)

    if len(visited) == N:
        ret = min(ret, s % K)

print(ret)
