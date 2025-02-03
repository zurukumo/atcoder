N, M, P = map(int, input().split())

v = [[] for _ in range(N)]
abc = []
for _ in range(M) :
    a, b, c = map(int, input().split())
    v[b-1].append((a-1, -(c-P)))
    
visited = [False] * N
visited[N-1] = True
queue = [N-1]
while queue :
    cur = queue.pop()
    for nex, cost in v[cur] :
        if not visited[nex] :
            queue.append(nex)
            visited[nex] = True
        abc.append((nex, cur, cost))
        
dist = [float('inf')] * N
dist[0] = 0

def bellmanford() :
    for i in range(N) :
        for a, b, c in abc :
            if dist[a] + c < dist[b] :
                dist[b] = dist[a] + c
                if i == N-1 :
                    return True
    return False
    
if bellmanford() :
    print(-1)
else :
    print(max(0, -dist[N-1]))
