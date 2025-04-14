import collections

N, M = map(int, input().split())
uv = [[int(i) for i in input().split()] for _ in range(M)]

graph = [[] for _ in range(N)]
for u, v in uv:
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

colors = [-1] * N
parity = [-1] * N
color = 0
for i in range(N):
    if colors[i] != -1:
        continue

    stack = [i]
    colors[i] = color
    parity[i] = 0
    while stack:
        cur = stack.pop()
        for nex in graph[cur]:
            if colors[nex] == -1:
                colors[nex] = color
                parity[nex] = 1 - parity[cur]
                stack.append(nex)
            elif colors[nex] != -1 and parity[nex] == parity[cur]:
                print(0)
                exit()
    color += 1

ret = 0
cnt1 = collections.defaultdict(int)
cnt2 = collections.defaultdict(int)
for i in range(N):
    cnt1[colors[i]] += 1
    cnt2[(colors[i], parity[i])] += 1

diff = 0
same = 0
for i in range(color):
    diff += cnt1[i] * (N - cnt1[i])
    same += cnt2[(i, 0)] * cnt2[(i, 1)]

ret = diff // 2 + same - M

print(ret)
