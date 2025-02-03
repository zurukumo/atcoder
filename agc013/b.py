import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
v = [[] for _ in range(N)]
for _ in range(M) :
    A, B = map(int, input().split())
    v[A-1].append(B-1)
    v[B-1].append(A-1)

visited = [False] * N
visited[0] = True
path = [[], []]

def dfs(cur, mode) :
    flag = True
    for nex in v[cur] :
        if visited[nex] :
            continue
            
        flag = False
        visited[nex] = True
        f = dfs(nex, mode)
        visited[nex] = False
        if f :
            path[mode].append(cur + 1)
            return True
        
    if flag :
        if mode == 0 :
            dfs(0, 1)
        path[mode].append(cur + 1)
        return True
    
    
    return False
        
dfs(0, 0)
ret = path[0][:-1] + path[1][::-1]
print(len(ret))
print(*ret)