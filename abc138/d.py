import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
v = [[] for _ in range(N)]
for _ in range(N-1) :
    a, b = map(int, input().split())
    v[a-1].append(b-1)
    v[b-1].append(a-1)
    
pq = [0 for _ in range(N)]
for _ in range(Q) :
    p, q = map(int, input().split())
    pq[p-1] += q
    
visited = [False] * N
visited[0] = True

ret = [0] * N
def bfs(cur, score) :
    ret[cur] = score + pq[cur]
    for nex in v[cur] :
        if not visited[nex] :
            visited[nex] = True
            bfs(nex, ret[cur])

bfs(0, 0)
    
print(*ret)