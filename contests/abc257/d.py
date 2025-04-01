N = int(input())
xyP = [[int(i) for i in input().split()] for _ in range(N)]

ng = -1
ok = 10**10


def check(s):
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            xi, yi, pi = xyP[i]
            xj, yj, pj = xyP[j]
            if pi * s >= abs(xi - xj) + abs(yi - yj):
                graph[i].append(j)

    for i in range(N):
        stack = [i]
        visited = [False] * N
        visited[i] = True
        while stack:
            cur = stack.pop()
            for nex in graph[cur]:
                if not visited[nex]:
                    visited[nex] = True
                    stack.append(nex)
        if all(visited):
            return True
    return False


while ok - ng > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
