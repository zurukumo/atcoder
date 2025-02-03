N = int(input())

uvw= [[int(i) for i in input().split()] for _ in range(N-1)]

path = [[] for _ in range(N+1)]

for u, v, w in uvw :
    path[u].append((v, w))
    path[v].append((u, w))

paint = [0] * (N + 1)

queue = [1]
visited = [False] * (N + 1)

while queue :
    current = queue.pop(0)
    w = paint[current]

    for destination, w_ in path[current] :
        if not visited[destination] :
            paint[destination] = (w + w_) & 1
            queue.append(destination)
            visited[destination] = True

for i in paint[1:] :
    print(i) 