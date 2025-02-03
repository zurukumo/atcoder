from heapq import heappush, heappop

N = int(input())
vec = [[] for _ in range(N)]
for i in range(N) :
    for j, v in enumerate(input()) :
        if v == '1' :
            vec[i].append(j)

def bfs(s) :
    dist = [float('inf')] * N
    queue = [(1, s)]
    dist[s] = 1
    
    while queue :
        co, cur = heappop(queue)
        if dist[cur] < co :
            continue
            
        for nex in vec[cur] :
            if co + 1 < dist[nex] :
                dist[nex] = co + 1
                heappush(queue, (co + 1, nex))
                
    for i in range(N) :
        for j in vec[i] :
            if abs(dist[i] - dist[j]) != 1 :
                return -1
    
    return max(dist)

ret = -1
for i in range(N) :
    ret = max(ret, bfs(i))
    
print(ret)