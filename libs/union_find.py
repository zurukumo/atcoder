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


class WeightedUnionFind:
    def __init__(self, N):
        self.parents = [-1] * N
        self.potential = [0] * N
        self.unites = N

    def root(self, x):
        while self.parents[x] >= 0:
            x = self.parents[x]
        return x

    def unite(self, x, y, w):
        rx = self.root(x)
        ry = self.root(y)

        if rx != ry:
            self.unites -= 1
            w = w + self.weight(x) - self.weight(y)
            if self.parents[rx] > self.parents[ry]:
                self.parents[rx] = ry
                self.potential[rx] = -w
            else:
                if self.parents[rx] == self.parents[ry]:
                    self.parents[rx] -= 1
                self.parents[ry] = rx
                self.potential[ry] = w

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.parents[self.root(x)]

    def weight(self, x):
        w = 0
        while self.parents[x] >= 0:
            w += self.potential[x]
            x = self.parents[x]
        return w

    def diff(self, x, y):
        return self.weight(y) - self.weight(x)
