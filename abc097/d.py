N, M = map(int, input().split())
p = [int(i) for i in input().split()]

v = [[] for _ in range(N)]
for _ in range(M) :
    x, y = map(int, input().split())
    v[x-1].append(y-1)
    v[y-1].append(x-1)
    
ret = 0
visited = [False] * N
for i in range(N) :
    if visited[i] :
        continue
    
    q = [i]
    visited[i] = True
    a = [i+1]
    b = [p[i]]
    
    while q :
        cur = q.pop()
        for nex in v[cur] :
            if visited[nex] :
                continue
            q.append(nex)
            a.append(nex+1)
            b.append(p[nex])
            visited[nex] = True
    ret += len(set(a) & set(b))
print(ret)