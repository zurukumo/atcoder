import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
uvw = [[int(i) for i in input().split()] for _ in range(M)]

vec = [[] for _ in range(N)]
for u, v, w in uvw:
    vec[u - 1].append((v - 1, w))
    vec[v - 1].append((u - 1, w))


def can_goal(x):
    visited = [False] * N
    visited[0] = True

    queue = [0]
    while queue:
        cur = queue.pop()
        for nex, w in vec[cur]:
            if not visited[nex] and (w & ~x) == 0:
                visited[nex] = True
                queue.append(nex)

    return visited[-1]


ret = (1 << 31) - 1
for i in range(30, -1, -1):
    if can_goal(ret ^ (1 << i)):
        ret ^= 1 << i

print(ret)
