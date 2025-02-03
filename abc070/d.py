import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
v = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    v[a - 1].append((b - 1, c))
    v[b - 1].append((a - 1, c))

visited = [-1] * N


def bfs(a, dist):
    for b, c in v[a]:
        if visited[b] < 0:
            visited[b] = dist + c
            bfs(b, dist + c)


Q, K = map(int, input().split())
visited[K - 1] = 0
bfs(K - 1, 0)
for _ in range(Q):
    x, y = map(int, input().split())
    print(visited[x - 1] + visited[y - 1])
