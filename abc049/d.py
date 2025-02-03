from collections import Counter
import sys
input = sys.stdin.readline

N, K, L = map(int, input().split())

vec1, vec2 = [[] for _ in range(N)], [[] for _ in range(N)]

for _ in range(K) :
    p, q = map(int, input().split())
    vec1[p-1].append(q-1)
    vec1[q-1].append(p-1)
for _ in range(L) :
    r, s = map(int, input().split())
    vec2[r-1].append(s-1)
    vec2[s-1].append(r-1)

def bfs(v) :
    visited = [-1] * N
    n = 0
    for i in range(N) :
        if visited[i] < 0 :
            queue = [i]
            visited[i] = n
            j = 0
            while j < len(queue) :
                cur = queue[j]
                for nex in v[cur] :
                    if visited[nex] < 0 :
                        queue.append(nex)
                        visited[nex] = n
                j += 1
            n += 1
            
    return visited
    
visited1 = bfs(vec1)
visited2 = bfs(vec2)
p = [(visited1[i], visited2[i]) for i in range(N)]
c = Counter(p)

print(' '.join([str(c[p[i]]) for i in range(N)]))