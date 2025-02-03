N, M = map(int, input().split())
ab = [[int(i) - 1 for i in input().split()] for _ in range(M)]

class UnionFind() :
    def __init__(self, N) :
        self.parent = [-1] * N
        
    def root(self, x) :
        while self.parent[x] >= 0:
            x = self.parent[x]
        return x

    def unite(self, x, y) :
        rx = self.root(x)
        ry = self.root(y)

        if rx != ry :
            if self.parent[rx] > self.parent[ry] :
                self.parent[rx] = ry
            else :
                if self.parent[rx] == self.parent[ry] :
                    self.parent[rx] -= 1
                self.parent[ry] = rx
    
    def same(self, x, y) :
        return self.root(x) == self.root(y)
        
    def size(self, x) :
        return -self.parent[self.root(x)]
        
UF = UnionFind(N)
for a, b in ab :
    UF.unite(a, b)
    
ret = 0
for p in UF.parent :
    if p < 0 :
        ret += 1
print(ret - 1)