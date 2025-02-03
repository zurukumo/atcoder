N, M = map(int, input().split())

vec = [[] for _ in range(N)]
for _ in range(M) :
    a, b = map(int, input().split())
    vec[a-1].append(b-1)
    vec[b-1].append(a-1)
    
visited = [False] * N

def bfs(cur, l) :
    if all(visited) :
        return 1
        
    ret = 0
    for nex in vec[cur] :
        if not visited[nex] :
            visited[nex] = True
            ret += bfs(nex, l + 1)
            visited[nex] = False
            
    return ret

visited[0] = True    
print(bfs(0, 0))