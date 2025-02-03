from bisect import bisect_left

N = int(input())
e5 = 10 ** 5

v = [[] for _ in range(2 * e5)]
visited = [True] * (2 * e5)

for _ in range(N) :
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    v[x].append(y + e5)
    v[y + e5].append(x)
    visited[x] = visited[y + e5] = False

ret = 0
for i in range(e5) :
    if not visited[i] :
        queue = [i]
        visited[i] = True
        nx, ny = 1, 0
        
        while queue :
            q = queue.pop()
            for j in v[q] :
                if not visited[j] :
                    visited[j] = True
                    queue.append(j)
                    
                    if j < e5 :
                        nx += 1
                    else :
                        ny += 1
                    
        ret += nx * ny
                    
print(ret - N)