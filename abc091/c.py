from collections import deque

N = int(input())
ab = [[int(i) for i in input().split()] for _ in range(N)]
cd = [[int(i) for i in input().split()] for _ in range(N)]

class FordFulkerson :
    # deque required
    def __init__(self, N) :
        self.N = N
        self.G = [[] for _ in range(N)]
        
    def add_edge(self, fr, to, cap) :
        self.G[fr].append([to, cap, len(self.G[to])])
        self.G[to].append([fr, 0, len(self.G[fr])-1])
        
    def bfs(self, fr, to) :
        self.pre_v = [0] * self.N
        self.pre_e = [0] * self.N
        visited = [False] * self.N
        visited[fr] = True
        
        q = deque([fr])
        while q :
            cur = q.popleft()
            
            for i, (nex, cap, _) in enumerate(self.G[cur]) :
                if visited[nex] or cap <= 0 :
                    continue
                
                self.pre_v[nex], self.pre_e[nex] = cur, i
                q.append(nex)
                visited[nex] = True
                
                if nex == to :
                    return True
                    
        return False
        
    def flow(self, fr, to) :
        ret = 0
        while self.bfs(fr, to) :
            cur = to
            min_cap = float('inf')
            while cur != fr :
                min_cap = min(min_cap, self.G[self.pre_v[cur]][self.pre_e[cur]][1])
                cur = self.pre_v[cur]
                
            ret += min_cap
            cur = to
            while cur != fr :
                self.G[self.pre_v[cur]][self.pre_e[cur]][1] -= min_cap
                self.G[cur][self.G[self.pre_v[cur]][self.pre_e[cur]][2]][1] += min_cap
                cur = self.pre_v[cur]
                
        return ret
        
FF = FordFulkerson(2 * N + 2)
for i in range(N) :
    FF.add_edge(0, i + 1, 1)
    FF.add_edge(i + N + 1, 2 * N + 1, 1)
    
for i, (a, b) in enumerate(ab) :
    for j, (c, d) in enumerate(cd) :
        if a < c and b < d :
            FF.add_edge(i + 1, j + N + 1, 1)

print(FF.flow(0, 2 * N + 1))