import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())

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
        
uf = UnionFind(N)        
AB = [[int(i) - 1 for i in input().split()] for _ in range(M)]
for A, B in AB :
    if not uf.same(A, B) :
        uf.unite(A, B)
    else :
        r = uf.root(A)
        ret = []
        for i in range(N) :
            if uf.root(i) == r :
                ret.append(i + 1)
        break
print(len(ret), ret)