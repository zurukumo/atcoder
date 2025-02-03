N, M, Q = map(int, input().split())
abc = [[int(i) for i in input().split()] for _ in range(M)]
uvw = [[int(i) for i in input().split()] for _ in range(Q)]


class UnionFind:
    def __init__(self, N):
        self.parent = [-1] * N

    def root(self, x):
        while self.parent[x] >= 0:
            x = self.parent[x]
        return x

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        if rx != ry:
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


ret = [-1] * Q

paths = []
for a, b, c in abc:
    paths.append((c, a - 1, b - 1, -1))
for i, (u, v, w) in enumerate(uvw):
    paths.append((w, u - 1, v - 1, i))

paths.sort()


uf = UnionFind(N)

for cost, fr, to, idx in paths:
    if uf.same(fr, to):
        if idx != -1:
            ret[idx] = "No"
    else:
        if idx != -1:
            ret[idx] = "Yes"
        else:
            uf.unite(fr, to)

for r in ret:
    print(r)
