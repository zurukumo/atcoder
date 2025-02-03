N, M, S = map(int, input().split())
vec = [[] for _ in range(N)]
for _ in range(M) :
    u, v = map(int, input().split())
    vec[u-1].append(v-1)
    vec[v-1].append(u-1)

visited = [False] * N

def search(s) :
    visited[s] = True
    q = [s]
    while q :
        cur = q.pop()
        for nex in vec[cur] :
            if nex >= s and not visited[nex] :
                visited[nex] = True
                q.append(nex)

search(S - 1)
ret = [S - 1]
for i in range(S - 2, -1, -1) :
    for j in vec[i] :
        if visited[j] :
            ret.append(i)
            search(i)
            break
    
ret.reverse()
for r in ret :
    print(r + 1)
