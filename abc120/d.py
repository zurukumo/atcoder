N, M = map(int, input().split())
AB = [[int(i)-1 for i in input().split()] for _ in range(M)]

class UnionFind() :
    def __init__(self, N) :
        self.parent = [-1] * N
        self.size = [1] * N
        self.rest = N * (N - 1) // 2
        
    def root(self, x) :
        while self.parent[x] >= 0:
            x = self.parent[x]
        return x

    def unite(self, x, y) :
        rx = self.root(x)
        ry = self.root(y)

        if rx != ry :
            self.rest -= self.size[rx] * self.size[ry]
            if self.parent[rx] > self.parent[ry] :
                self.parent[rx] = ry
                self.size[ry] += self.size[rx]
            else :
                if self.parent[rx] == self.parent[ry] :
                    self.parent[rx] -= 1
                self.parent[ry] = rx
                self.size[rx] += self.size[ry]
                
ret = [0] * M
UF = UnionFind(N)
for i in range(M-1, -1, -1) :
    a, b = AB[i] 
    ret[i] = UF.rest
    UF.unite(a, b)
for i in range(M) :
    print(ret[i])