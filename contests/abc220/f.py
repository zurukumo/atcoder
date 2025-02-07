import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
uv = [[int(i) for i in input().split()] for _ in range(N - 1)]

G = [[] for _ in range(N)]
for u, v in uv:
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

ret = [0] * N
size = [0] * N


# 部分木のサイズを計算
def dfs(pre, cur):
    x = 0
    for nex in G[cur]:
        if nex == pre:
            continue

        t = dfs(cur, nex)
        x += t

    size[cur] = x
    return x + 1


dfs(-1, 0)


s = 0
queue = [(-1, 0, 0)]
while queue:
    pre, cur, depth = queue.pop()
    s += depth

    for i, nex in enumerate(G[cur]):
        if nex == pre:
            continue

        queue.append((cur, nex, depth + 1))


queue = [(-1, 0, s)]
ret = [-1] * N
while queue:
    pre, cur, cost = queue.pop()
    ret[cur] = cost

    for i, nex in enumerate(G[cur]):
        if nex == pre:
            continue

        queue.append((cur, nex, cost - (size[nex] + 1) + (N - size[nex] - 1)))

for i in range(N):
    print(ret[i])
