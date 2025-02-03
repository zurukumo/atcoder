N, M = map(int, input().split())
P = [int(i) - 1 for i in input().split()]

mod = 998244353


class UnionFind:
    def __init__(self, N):
        self.parent = [-1] * N
        self.units = N

    def root(self, x):
        while self.parent[x] >= 0:
            x = self.parent[x]
        return x

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        if rx != ry:
            self.units -= 1
            if self.parent[rx] > self.parent[ry]:
                self.parent[rx] = ry
            else:
                if self.parent[rx] == self.parent[ry]:
                    self.parent[rx] -= 1
                self.parent[ry] = rx

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.parent[self.root(x)]


uf = UnionFind(N)

ret = 0
for a, b in enumerate(P):
    if not uf.same(a, b):
        ret += M * (M - 1) // 2 * pow(M, uf.units - 2, mod)
        ret %= mod
    uf.unite(a, b)

print(ret)
