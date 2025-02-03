import sys

input = sys.stdin.readline

N, M = map(int, input().split())

v = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    v[a - 1].append(b - 1)
    v[b - 1].append(a - 1)

q1 = [0]
q2 = []
visited = [False] * N
visited[0] = True

while q1:
    cur = q1.pop()
    for nex in v[cur]:
        if not visited[nex]:
            visited[nex] = True
            q2.append(nex)

while q2:
    cur = q2.pop()
    for nex in v[cur]:
        if not visited[nex]:
            visited[nex] = True

if visited[N - 1]:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
