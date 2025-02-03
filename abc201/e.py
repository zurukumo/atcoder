import sys

input = sys.stdin.readline

N = int(input())
uvw = [[int(i) for i in input().split()] for _ in range(N - 1)]

mod = 10**9 + 7

vec = [[] for _ in range(N)]
for u, v, w in uvw:
    u, v = u - 1, v - 1
    vec[u].append((v, w))
    vec[v].append((u, w))

queue = [0]
visited = [False] * N
weight = [0] * N
visited[0] = True
while queue:
    cur = queue.pop()
    for nex, w in vec[cur]:
        if visited[nex]:
            continue

        queue.append(nex)
        visited[nex] = True
        weight[nex] = weight[cur] ^ w

digit = [0] * 70
for w in weight:
    for i in range(70):
        if w & (1 << i):
            digit[i] += 1

ret = 0
for i in range(70):
    ret += digit[i] * (N - digit[i]) * (1 << i) % mod
    ret %= mod

print(ret)
