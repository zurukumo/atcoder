from itertools import permutations

N, M, R = map(int, input().split())
r = [int(i)-1 for i in input().split()]
v = [[] for _ in range(N)]
for _ in range(M) :
    A, B, C = map(int, input().split())
    v[A-1].append((B-1, C))
    v[B-1].append((A-1, C))

def dijkstra(s) :
    queue = [(s, 0)]
    dist = [float('inf')] * N
    dist[s] = 0
    while queue :
        cur, ccost = queue.pop()
        for nex, ncost in v[cur] :
            if ccost + ncost < dist[nex] :
                dist[nex] = ccost + ncost
                queue.append((nex, ccost + ncost))
    return dist
    
dist = dict()
for rr in r :
    dist[rr] = dijkstra(rr)

lr = len(r)
m = float('inf')
for perm in permutations(r) :
    tot = 0
    for i in range(lr-1) :
        tot += dist[perm[i]][perm[i+1]]
    m = min(m, tot)
    
print(m)