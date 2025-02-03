from collections import deque

N, M = map(int, input().split())

vec = [[] for _ in range(N)]
for _ in range(M) :
    u, v = map(int, input().split())
    vec[u-1].append(v-1)

S, T = map(int, input().split())
S, T = S - 1, T - 1

visited = [[False] * N for _ in range(3)]
visited[0][S] = True
queue = deque([(S, 0)])

while queue :
    q, cost = queue.popleft()
    p = (cost + 1) % 3
    for i in vec[q] :
        if p == 0 and i == T :
            print((cost + 1) // 3)
            exit()
        if not visited[p][i] :
            visited[p][i] = True
            queue.append((i, cost + 1))

print(-1)
    