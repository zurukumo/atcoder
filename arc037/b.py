import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
vec = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    vec[u - 1].append(v - 1)
    vec[v - 1].append(u - 1)


def bfs(cur, pre):
    flag = True
    for nex in vec[cur]:
        if nex == pre:
            continue
        if visited[nex]:
            flag = False
        else:
            visited[nex] = True
            flag = flag and bfs(nex, cur)
    return flag


ret = 0
visited = [False] * N
for i in range(N):
    if not visited[i]:
        visited[i] = True
        if bfs(i, -1):
            ret += 1

print(ret)
