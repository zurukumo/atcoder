N, M = map(int, input().split())
v = [[] for _ in range(N)]
u = [[] for _ in range(N)]
for _ in range(N + M - 1) :
    A, B = map(int, input().split())
    v[A-1].append(B-1)
    u[B-1].append(A-1)

for i in range(N) :
    if len(u[i]) == 0 :
        s = i
        break
        
dist = [0] * N
par = [-1] * N
cnt = [0] * N

par[s] = -1
q = [s]
while q :
    cur = q.pop()
    cnt[cur] += 1
    if cur != s and cnt[cur] != len(u[cur]) :
        continue
        
    for nex in v[cur] :
        if dist[cur] + 1 > dist[nex] :
            dist[nex] = dist[cur] + 1
            par[nex] = cur
            q.append((nex))

for i in range(N) :
    print(par[i] + 1)