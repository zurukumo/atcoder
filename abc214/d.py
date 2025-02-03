import sys

sys.setrecursionlimit(10**7)

N = int(input())
uvw = [[int(i) for i in input().split()] for _ in range(N - 1)]


class UnionFind:
    def __init__(self, N):
        self.parents = [-1] * N
        self.sizes = [1] * N
        self.units = N

    def root(self, x):
        while self.parents[x] >= 0:
            x = self.parents[x]
        return x

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        if rx != ry:
            self.units -= 1
            if self.parents[rx] > self.parents[ry]:
                self.parents[rx] = ry
                self.sizes[ry] += self.sizes[rx]
            else:
                if self.parents[rx] == self.parents[ry]:
                    self.parents[rx] -= 1
                self.parents[ry] = rx
                self.sizes[rx] += self.sizes[ry]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def height(self, x):
        return -self.parents[self.root(x)]

    def size(self, x):
        return self.sizes[self.root(x)]


uvw.sort(key=lambda x: x[2])

ret = 0
uf = UnionFind(N)
for u, v, w in uvw:
    u -= 1
    v -= 1
    ret += w * uf.size(u) * uf.size(v)
    uf.unite(u, v)

print(ret)
