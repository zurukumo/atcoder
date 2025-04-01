import collections

N, M = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(M)]
Q = int(input())
xk = [[int(i) for i in input().split()] for _ in range(Q)]

graph = [[] for _ in range(N)]
for a, b in ab:
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

for x, k in xk:
    x -= 1
    done = dict()
    queue = collections.deque([x])
    done[x] = 0
    while queue:
        cur = queue.popleft()
        for nex in graph[cur]:
            if nex not in done and done[cur] < k:
                done[nex] = done[cur] + 1
                if done[nex] < k:
                    queue.append(nex)

    print(sum(k + 1 for k in done.keys()))
