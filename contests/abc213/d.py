import heapq
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N - 1)]

vec = [[] for _ in range(N)]
for a, b in AB:
    heapq.heappush(vec[a - 1], (b - 1))
    heapq.heappush(vec[b - 1], (a - 1))

ret = []
visited = [False] * N


def dfs(cur):
    while vec[cur]:
        nex = heapq.heappop(vec[cur])
        if not visited[nex]:
            ret.append(nex)
            visited[nex] = True
            dfs(nex)
            ret.append(cur)


ret.append(0)
visited[0] = True
dfs(0)

print(*[r + 1 for r in ret])
