N, M = map(int, input().split())
v = [[] for _ in range(N)]
for i in range(M) :
    a, b = map(int, input().split())
    v[a-1].append((b-1, i))
    v[b-1].append((a-1, i))

def dfs(n) :
    queue = [0]
    visited = [False] * N
    visited[0] = True
    counter = 1
    while queue :
        cur = queue.pop()
        for nex, i in v[cur] :
            if i == n : 
                continue
            if not visited[nex] :
                counter += 1
                queue.append(nex)
                visited[nex] = True
    
    return counter != N

ret = 0
for i in range(M) :
    if dfs(i) :
        ret += 1
print(ret)