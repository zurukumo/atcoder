N, K = map(int, input().split())
a = [[int(i) for i in input().split()] for _ in range(N)]

mod = 998244353


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


row_uf = UnionFind(N)
col_uf = UnionFind(N)

for i in range(N):
    for j in range(i + 1, N):
        if all(a[i][k] + a[j][k] <= K for k in range(N)):
            row_uf.unite(i, j)
        if all(a[k][i] + a[k][j] <= K for k in range(N)):
            col_uf.unite(i, j)

ret = 1
for i in range(N):
    if row_uf.parents[i] < 0:
        for j in range(1, row_uf.size(i) + 1):
            ret *= j
            ret %= mod
    if col_uf.parents[i] < 0:
        for j in range(1, col_uf.size(i) + 1):
            ret *= j
            ret %= mod

print(ret)
